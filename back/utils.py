import os
import json
import random
import warnings
import numpy as np
import imagehash
import heapq
import seaborn as sns
from math import exp
from pandas import DataFrame
from json import JSONEncoder
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from functools import reduce
from PIL import Image
from skimage.measure import compare_ssim
from sklearn import manifold
from sklearn.preprocessing import normalize
from nltk.corpus import wordnet as wn
import base64
import scipy.ndimage
from scipy.ndimage.filters import gaussian_filter

warnings.filterwarnings("ignore")


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

def drawContour(cam_name, cam_path, contour_path, th):
    cam_np = np.load(cam_path)
    if cam_name != 'BBMP':
        cam_np = cam_np / 255.
    if len(cam_np.shape) == 3:
        cam_np = cam_np[:, :, 0]
    levels = np.arange(th, 1, (1 - th) / 4)
    # cam_np = scipy.ndimage.zoom(cam_np, 5.0)
    cam_np = gaussian_filter(cam_np, sigma=5)
    cam_np_mask = np.ma.masked_where(cam_np < levels[-1], cam_np)

    plt.figure(figsize=(5, 5))
    contours = plt.contour(cam_np, levels, colors='black')
    plt.clabel(contours, inline=True, fontsize=15)
    plt.imshow(cam_np_mask, cmap='viridis', origin='upper', alpha=0.5, interpolation='nearest')
    # plt.colorbar()
    plt.gca().set_aspect('1.0')
    plt.axis('off')
    plt.savefig(contour_path, bbox_inches=0)
    with open(contour_path, 'rb') as imgf:
        contour_data = base64.b64encode(imgf.read()).decode('utf-8')
    return contour_data

def getFilteredCamImg(cam_name, cam_path, cam_img_path, filtered_path, th):
    with open(cam_img_path, 'rb') as imgf:
        org_data = base64.b64encode(imgf.read()).decode('utf-8')
    image = Image.open(cam_img_path).convert('RGB').resize((224, 224))
    img = np.array(image)
    cam_np = np.load(cam_path)
    if cam_name != 'BBMP':
        cam_np = cam_np / 255.
    idx_list = []
    for i in range(cam_np.shape[0]):
        for j in range(cam_np.shape[1]):
            mask_value = cam_np[i, j]
            if mask_value < th:
                img[i, j, 0] = 255
                img[i, j, 1] = 255
                img[i, j, 2] = 255
                cur_idx = [i, j]
                idx_list.append(cur_idx)
    im = Image.fromarray(img)
    im.save(filtered_path)
    with open(filtered_path, 'rb') as imgf:
        filtered_data = base64.b64encode(imgf.read()).decode('utf-8')
    return org_data, filtered_data

def idxToWord(dataset_path, label_idx):
    with open(os.path.join(dataset_path, 'idxToWord.json'), 'r') as f:
        pattern_idxToWord = json.loads(f.read())
    if str(label_idx) in pattern_idxToWord:
        label_content = pattern_idxToWord[str(label_idx)]
    else:
        print('WRONG!')
    return label_content


def idxToID(dataset_path, label_idx):
    with open(os.path.join(dataset_path, 'idxtoIDTotal.json'), 'r') as f:
        pattern_idxToID = json.loads(f.read())
    if str(label_idx) in pattern_idxToID:
        wordID = pattern_idxToID[str(label_idx)]
    else:
        print(label_idx, 'WRONG!')
    return wordID


def IDtoIdx(dataset_path, label_ID):
    with open(os.path.join(dataset_path, 'IDtoIdxTotal.json'), 'r') as f:
        pattern_idxToID = json.loads(f.read())
    if str(label_ID) in pattern_idxToID:
        labelIdx = int(pattern_idxToID[str(label_ID)])
    else:
        print(label_ID, 'WRONG!')
    return labelIdx


def IDToWord(dataset_path, wordID):
    with open(os.path.join(dataset_path, 'id_word.json'), 'r') as f:
        pattern_IDToWord = json.loads(f.read())
    if str(wordID) in pattern_IDToWord:
        word = pattern_IDToWord[str(wordID)]
    else:
        print(wordID, 'WRONG!')
    return word


def findParentLabel(dataset_path, wordID):
    with open(os.path.join(dataset_path, 'IDtoParentIDTotal.json'), 'r') as f:
        pattern_findParentLabel = json.loads(f.read())

    if str(wordID) in pattern_findParentLabel:
        parentWordID = pattern_findParentLabel[str(wordID)]
        # if not isinstance(parentWordID, list):
        #     print(parentWordID, 'wrong!!!')
    else:
        print(wordID, 'WRONG!')
    return parentWordID


def processWrong(expModel, dataset_path):
    # wrongImgs = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{expModel}', 'wrong_name.npy')).tolist()
    wrong_rel_label = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{expModel}', 'wrong_rel_label.npy')).tolist()
    wrong_prd_label = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{expModel}', 'wrong_prd_label.npy')).tolist()
    wrong_probability = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{expModel}', 'wrong_probability.npy')).tolist()

    # print(len(wrongImgs))

    # wrong_count = list(0 for i in range(1000))
    # wrong_sameParent_count = list(0 for i in range(1000))
    # wrong_diffParent_count = list(0 for i in range(1000))

    # wrong_sameParent_name = []
    # wrong_sameParent_rel_label = []
    # wrong_sameParent_prd_label = []
    wrong_sameParent_probability = []
    # wrong_diffParent_name = []
    # wrong_diffParent_rel_label = []
    # wrong_diffParent_prd_label = []
    wrong_diffParent_probability = []
    for i in range(len(wrong_rel_label)):
        rel_label = wrong_rel_label[i]
        prd_label = wrong_prd_label[i]
        # wrong_count[rel_label] += 1

        rel_label_ID = idxToID(dataset_path, rel_label)
        prd_label_ID = idxToID(dataset_path, prd_label)

        pr_rel_label = findParentLabel(dataset_path, rel_label_ID)
        pr_prd_label = findParentLabel(dataset_path, prd_label_ID)
        pr_common = list(set(pr_rel_label) & set(pr_prd_label))
        if len(pr_common) == 0:
            # wrong_diffParent_name.append(wrongImgs[i])
            # wrong_diffParent_rel_label.append(wrong_rel_label[i])
            # wrong_diffParent_prd_label.append(wrong_prd_label[i])
            wrong_diffParent_probability.append(wrong_probability[i])
            # wrong_diffParent_count[rel_label] += 1
            # rel_label_content = IDToWord(dataset_path, rel_label_ID)
            # prd_label_content = IDToWord(dataset_path, prd_label_ID)
            # print(rel_label_content, 'VS', prd_label_content)
        else:
            # wrong_sameParent_name.append(wrongImgs[i])
            # wrong_sameParent_rel_label.append(wrong_rel_label[i])
            # wrong_sameParent_prd_label.append(wrong_prd_label[i])
            wrong_sameParent_probability.append(wrong_probability[i])
            # wrong_sameParent_count[rel_label] += 1
            # rel_label_content = IDToWord(dataset_path, rel_label_ID)
            # prd_label_content = IDToWord(dataset_path, prd_label_ID)
            # print(rel_label_content, '----', prd_label_content)
            # for l in pr_common:
            #     print('----', IDToWord(dataset_path, l))
    # print(len(wrong_diffParent_name))
    # print(len(wrong_sameParent_name))
    # np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{expModel}', 'wrong_sameParent_name.npy'), wrong_sameParent_name)
    # np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{expModel}', 'wrong_sameParent_rel_label.npy'), wrong_sameParent_rel_label)
    # np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{expModel}', 'wrong_sameParent_prd_label.npy'), wrong_sameParent_prd_label)
    # np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{expModel}', 'wrong_sameParent_count.npy'), wrong_sameParent_count)
    np.save(os.path.join(dataset_path, 'ImageNet_Val',
                         f'model.{expModel}', 'wrong_sameParent_probability.npy'), wrong_sameParent_probability)

    # np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{expModel}', 'wrong_diffParent_name.npy'), wrong_diffParent_name)
    # np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{expModel}', 'wrong_diffParent_rel_label.npy'), wrong_diffParent_rel_label)
    # np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{expModel}', 'wrong_diffParent_prd_label.npy'), wrong_diffParent_prd_label)
    # np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{expModel}', 'wrong_diffParent_count.npy'), wrong_diffParent_count)
    np.save(os.path.join(dataset_path, 'ImageNet_Val',
                         f'model.{expModel}', 'wrong_diffParent_probability.npy'), wrong_diffParent_probability)

    # for j in range(len(wrong_sameParent_count)):
    #     if wrong_sameParent_count[j] != 0 and wrong_diffParent_count[j] != 0:
    #         print(j, wrong_count[j], wrong_sameParent_count[j], wrong_diffParent_count[j])

    # print(len(same_p1))
    # print(len(same_p2))
    # print(len(same_p3))
    # print(len(same_p4))
    # print(len(same_p5))
    # print(len(same_pm))


def findLabelAcc(model_name, dataset_path):
    accuracy = np.load(os.path.join(dataset_path, 'ImageNet_Val',
                                    f'model.{model_name}', 'accuracy.npy')).tolist()
    overall = accuracy[1000]
    print(overall)

    del accuracy[1000]

    min_acc = min(accuracy)
    max_acc = max(accuracy)

    min_acc_list = []
    min_acc_idx = []
    max_acc_list = []
    max_acc_idx = []

    for i in range(len(accuracy)):
        acc = accuracy[i]
        if acc == min_acc:
            min_acc_list.append(acc)
            min_acc_idx.append(i)
        elif acc == max_acc:
            max_acc_list.append(acc)
            max_acc_idx.append(i)
    print(len(min_acc_list))
    print(len(min_acc_idx))
    print(len(max_acc_list))
    print(len(max_acc_idx))

    # max_acc = heapq.nlargest(5, accuracy)
    # max_idx = map(accuracy.index, heapq.nlargest(5, accuracy))
    # min_acc = heapq.nsmallest(5, accuracy)
    # min_idx = map(accuracy.index, heapq.nsmallest(5, accuracy))

    # print(max_acc)
    # print(list(max_idx))
    # print(min_acc)
    # print(list(min_idx))


def findCorWro(expModel, dataset_path, total_img):
    correctImgs = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{expModel}', 'correct_name.npy'))
    label = np.load(os.path.join(dataset_path, 'ImageNet_Val',
                                 f'model.{expModel}', 'label.npy'))
    prd_label = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{expModel}', 'predicted.npy'))
    probability = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{expModel}', 'probability.npy'))

    correct_label = []
    wrongImgs = []
    wrongProbability = []
    wrong_rel_label = []
    wrong_prd_label = []
    for i in range(len(total_img)):
        img_name = total_img[i]
        if img_name not in correctImgs:
            wrongImgs.append(img_name)
            wrongProbability.append(probability[i])
            wrong_rel_label.append(label[i])
            wrong_prd_label.append(prd_label[i])
            if label[i] == prd_label[i]:
                print('Wrong wrong list')
        else:
            if label[i] == prd_label[i]:
                correct_label.append(prd_label[i])
            else:
                print('Wrong correct list')

    print(len(correct_label))
    print(len(correctImgs))

    print(len(wrongImgs))
    print(len(wrongProbability))
    print(len(wrong_rel_label))
    print(len(wrong_prd_label))

    np.save(os.path.join(dataset_path, 'ImageNet_Val',
                         f'model.{expModel}', 'wrong_name.npy'), wrongImgs)
    np.save(os.path.join(dataset_path, 'ImageNet_Val',
                         f'model.{expModel}', 'wrong_probability.npy'), wrongProbability)
    np.save(os.path.join(dataset_path, 'ImageNet_Val',
                         f'model.{expModel}', 'wrong_rel_label.npy'), wrong_rel_label)
    np.save(os.path.join(dataset_path, 'ImageNet_Val',
                         f'model.{expModel}', 'wrong_prd_label.npy'), wrong_prd_label)
    np.save(os.path.join(dataset_path, 'ImageNet_Val',
                         f'model.{expModel}', 'correct_label.npy'), correct_label)


def getMultiClassInfo(dataset_path, exampleModel, input_labels):
    accuracy = np.load(os.path.join(dataset_path, 'ImageNet_Val',
                                    f'model.{exampleModel}', 'accuracy.npy')).tolist()
    correct_label = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'correct_label.npy')).tolist()
    correct_name = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'correct_name.npy')).tolist()
    correct_probability = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'correct_probability.npy')).tolist()
    wrong_sameParent_rel_label = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_sameParent_rel_label.npy')).tolist()
    wrong_sameParent_prd_label = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_sameParent_prd_label.npy')).tolist()
    wrong_sameParent_name = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_sameParent_name.npy')).tolist()
    wrong_sameParent_probability = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_sameParent_probability.npy')).tolist()
    wrong_diffParent_rel_label = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_diffParent_rel_label.npy')).tolist()
    wrong_diffParent_prd_label = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_diffParent_prd_label.npy')).tolist()
    wrong_diffParent_name = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_diffParent_name.npy')).tolist()
    wrong_diffParent_probability = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_diffParent_probability.npy')).tolist()
    label_num = len(input_labels)
    example_names = []
    example_rel = []
    example_acc = []
    example_prd = []
    example_certainty = []
    for j in range(label_num):
        correct_count = 0
        wrong_count = 0
        for i in range(len(correct_label)):
            if correct_label[i] == input_labels[j]:
                example_names.append(correct_name[i])
                example_rel.append(idxToWord(dataset_path, correct_label[i]))
                example_acc.append(accuracy[correct_label[i]])
                example_prd.append(idxToWord(dataset_path, correct_label[i]))
                example_certainty.append(correct_probability[i])
                correct_count += 1
                break
        for i in range(len(wrong_sameParent_rel_label)):
            if wrong_sameParent_rel_label[i] == input_labels[j]:
                example_names.append(wrong_sameParent_name[i])
                example_rel.append(
                    idxToWord(dataset_path, wrong_sameParent_rel_label[i]))
                example_acc.append(accuracy[wrong_sameParent_rel_label[i]])
                example_prd.append(
                    idxToWord(dataset_path, wrong_sameParent_prd_label[i]))
                example_certainty.append(wrong_sameParent_probability[i])
                wrong_count += 1
                break
        for i in range(len(wrong_diffParent_name)):
            if wrong_diffParent_rel_label[i] == input_labels[j]:
                example_names.append(wrong_diffParent_name[i])
                example_rel.append(
                    idxToWord(dataset_path, wrong_diffParent_rel_label[i]))
                example_acc.append(accuracy[wrong_diffParent_rel_label[i]])
                example_prd.append(
                    idxToWord(dataset_path, wrong_diffParent_prd_label[i]))
                example_certainty.append(wrong_diffParent_probability[i])
                wrong_count += 1
                break
    return example_names, example_rel, example_acc, example_prd, example_certainty


def task1ImgSelection(dataset_path, input_label):
    task1_path = os.path.join(dataset_path, 'ImageNet_Val', 'task1_info')
    correct_list = np.load(os.path.join(
        task1_path, f'label_{input_label}_correct.npy')).tolist()
    wrong_list = np.load(os.path.join(
        task1_path, f'label_{input_label}_wrong.npy')).tolist()
    combo_list = np.load(os.path.join(
        task1_path, f'label_{input_label}_combo.npy')).tolist()
    random.seed(10)
    try:
        wrong_name = random.sample(wrong_list, 5)
        try:
            combo_name = random.sample(combo_list, 5)
            try:
                corract_name = random.sample(correct_list, 2)
            except(ValueError):
                corract_name = random.sample(correct_list, len(correct_list))
        except(ValueError):
            combo_name = random.sample(combo_list, len(combo_list))
            try:
                corract_name = random.sample(correct_list, 2)
            except(ValueError):
                corract_name = random.sample(correct_list, len(correct_list))
    except(ValueError):
        wrong_name = random.sample(wrong_list, len(wrong_list))
        try:
            combo_name = random.sample(combo_list, 6)
            try:
                corract_name = random.sample(correct_list, 2)
            except(ValueError):
                corract_name = random.sample(correct_list, len(correct_list))
        except(ValueError):
            combo_name = random.sample(combo_list, len(combo_list))
            try:
                corract_name = random.sample(correct_list, 2)
            except(ValueError):
                corract_name = random.sample(correct_list, len(correct_list))
    out_imgname = []
    out_imgname.extend(corract_name)
    out_imgname.extend(wrong_name)
    out_imgname.extend(combo_name)
    print(f'inputlabel: {input_label}\t{len(out_imgname)}')
    np.save(os.path.join(dataset_path, 'ImageNet_Val', 'task1_info',
                         f'label_{input_label}_task1examplename.npy'), out_imgname)


def task1ImgGeneration(model_list, dataset_path):
    correct_lists = ()
    wrong_lists = ()
    # wrong_same_lists = ()
    # wrong_diff_lists = ()
    out_path = os.path.join(dataset_path, 'ImageNet_Val', 'task1_info')
    os.makedirs(out_path, exist_ok=True)
    for i in range(len(model_list)):
        model_name = model_list[i]
        correct_list = np.load(os.path.join(
            dataset_path, 'ImageNet_Val', f'model.{model_name}', 'correct_name.npy'))
        wrong_list = np.load(os.path.join(
            dataset_path, 'ImageNet_Val', f'model.{model_name}', 'wrong_name.npy'))
        # wrong_same_list = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'wrong_sameParent_name.npy'))
        # wrong_diff_list = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'wrong_diffParent_name.npy'))
        correct_lists += (correct_list,)
        wrong_lists += (wrong_list,)
        # wrong_same_lists += (wrong_same_list,)
        # wrong_diff_lists += (wrong_diff_list,)

    correct_comb = reduce(np.intersect1d, correct_lists)
    wrong_comb = reduce(np.intersect1d, wrong_lists)
    # wrong_same_comb = reduce(np.intersect1d, wrong_same_lists)
    # wrong_diff_comb = reduce(np.intersect1d, wrong_diff_lists)
    combo_comb = []
    name_list = np.load(os.path.join(dataset_path, 'name.npy')).tolist()
    for i in range(len(name_list)):
        name = name_list[i]
        if name not in correct_comb and name not in wrong_comb:
            combo_comb.append(name)
    np.save(os.path.join(out_path, 'total_allcorrect.npy'), correct_comb)
    np.save(os.path.join(out_path, 'total_allwrong.npy'), wrong_comb)
    np.save(os.path.join(out_path, 'total_correctandwrong.npy'), combo_comb)


def task1ImgGet(out_path, label_list, name_list, correct_comb, wrong_comb, both_comb):
    for input_label in range(800, 1000):
        out_correct = []
        out_wrong = []
        out_combo = []
        for i in range(len(name_list)):
            name = name_list[i]
            label = label_list[i]
            if name in correct_comb and label == input_label:
                out_correct.append(name)
            if name in wrong_comb and label == input_label:
                out_wrong.append(name)
            if name in both_comb and label == input_label:
                out_combo.append(name)
        np.save(os.path.join(
            out_path, f'label_{input_label}_correct.npy'), out_correct)
        np.save(os.path.join(
            out_path, f'label_{input_label}_wrong.npy'), out_wrong)
        np.save(os.path.join(
            out_path, f'label_{input_label}_combo.npy'), out_combo)
        print(
            f'label:{input_label}--- [{len(out_correct), len(out_wrong), len(out_combo)}]')

    # count = np.zeros([1000, 5], int)
    # for i in range(len(name_list)):
    #     name = name_list[i]
    #     label = label_list[i]
    #     if name in correct_comb:
    #         count[label, 0] += 1
    #     elif name in wrong_comb:
    #         count[label, 1] += 1
    #     else:
    #         count[label, 2] += 1
    #     if name in wrong_same_comb:
    #         count[label, 2] += 1
    #     if name in wrong_diff_comb:
    #         count[label, 4] += 1
    # for i in range(count.shape[0]):
    #     print(f'label:{i}--- {count[i]}')

    # correct_comb_label = []
    # wrong_comb_label = []
    # wrong_same_comb_label = []
    # wrong_diff_comb_label = []
    # cor_wrong_comb_label = []
    # for i in range(len(name_list)):
    #     name = name_list[i]
    #     label = label_list[i]
    #     if name in correct_comb:
    #         correct_comb_label.append(label)
    #     elif name in wrong_comb:
    #         wrong_comb_label.append(label)
    #     else:
    #         cor_wrong_comb.append(name)
    #         cor_wrong_comb_label.append(label)
    #     if name in wrong_same_comb:
    #         wrong_same_comb_label.append(label)
    #     if name in wrong_diff_comb:
    #         wrong_diff_comb_label.append(label)
    # print(len(correct_comb), len(correct_comb_label))
    # print(len(wrong_comb), len(wrong_comb_label))
    # print(len(cor_wrong_comb), len(cor_wrong_comb_label))
    # print(len(wrong_same_comb), len(wrong_same_comb_label))
    # print(len(wrong_diff_comb), len(wrong_diff_comb_label))


def task2ImgGeneration(dataset_path, model_name, input_labels):
    out_path = os.path.join(dataset_path, 'ImageNet_Val',
                            'task2_info', f'model.{model_name}')
    task2_names = []
    for input_label in input_labels:
        print(input_label, type(input_label))
        # if input_label == '238':
        #     names = ['ILSVRC2012_val_00000531.JPEG', 'ILSVRC2012_val_00003139.JPEG', 'ILSVRC2012_val_00021642.JPEG']
        #     np.save(os.path.join(out_path, f'label_{input_label}_task2examplename.npy'), names)
        names = np.load(os.path.join(
            out_path, f'label_{input_label}_task2examplename.npy')).tolist()
        task2_names.extend(names)
    return task2_names

def task2FullImg(dataset_path, input_labels):
    # label_list = np.load(os.path.join(dataset_path, 'label.npy'))
    # name_list = np.load(os.path.join(dataset_path, 'name.npy'))
    # print(len(label_list), label_list[50], type(label_list[50]))
    # print(len(name_list), name_list[50], type(name_list[50]))
    # for input_label in range(1000):
    #     label_img = []
    #     for i in range(len(label_list)):
    #         if label_list[i] == input_label:
    #             label_img.append(name_list[i])
    #     print(f'label: {input_label}, total image: {len(label_img)}')
    #     np.save(os.path.join(dataset_path, 'ImageNet_Val', 'total_imgList', f'label_{input_label}_full_imgname.npy'), label_img)
    task2_names = []
    for input_label in input_labels:
        names = np.load(os.path.join(dataset_path, 'ImageNet_Val', 'total_imgList', f'label_{input_label}_full_imgname.npy')).tolist()
        print(f'label: {input_label}, total image: {len(names)}')
        task2_names.extend(names)
    return task2_names

def task2ImgGet(dataset_path, exampleModel):
    # accuracy = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'accuracy.npy')).tolist()
    out_path = os.path.join(dataset_path, 'ImageNet_Val',
                            'task2_info', f'model.{exampleModel}')
    total_names = []
    for input_label in (range(1000)):
        names = np.load(os.path.join(
            out_path, f'label_{input_label}_task2examplename.npy')).tolist()
        total_names.extend(names)
    np.save(os.path.join(out_path, 'task2examplenameTotal.npy'), total_names)
    print(len(total_names))

    # random.seed(10)
    # if accuracy[input_label] == 100:
    #     corr_name = np.load(os.path.join(out_path, f'label_{input_label}_correct_name.npy')).tolist()
    #     names = random.sample(corr_name, 3)
    # else:
    #     corr_name = np.load(os.path.join(out_path, f'label_{input_label}_correct_name.npy')).tolist()
    #     wrong_same_name = np.load(os.path.join(out_path, f'label_{input_label}_wrong_same_name.npy')).tolist()
    #     wrong_diff_name = np.load(os.path.join(out_path, f'label_{input_label}_wrong_diff_name.npy')).tolist()
    #     if len(wrong_same_name) == 0:
    #         if len(wrong_diff_name) < 2:
    #             name1 = random.sample(corr_name, 2)
    #             name2 = []
    #             name3 = random.sample(wrong_diff_name, 1)
    #         else:
    #             name1 = random.sample(corr_name, 1)
    #             name2 = []
    #             name3 = random.sample(wrong_diff_name, 2)
    #     elif len(wrong_diff_name) == 0:
    #         if len(wrong_same_name) < 2:
    #             name1 = random.sample(corr_name, 2)
    #             name2 = random.sample(wrong_same_name, 1)
    #             name3 = []
    #         else:
    #             name1 = random.sample(corr_name, 1)
    #             name2 = random.sample(wrong_same_name, 2)
    #             name3 = []
    #     else:
    #         name1 = random.sample(corr_name, 1)
    #         name2 = random.sample(wrong_same_name, 1)
    #         name3 = random.sample(wrong_diff_name, 1)
    #     names = name1 + name2 + name3
    # np.save(os.path.join(out_path, f'label_{input_label}_task2examplename.npy'), names)

    # accuracy = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'accuracy.npy')).tolist()
    # correct_label = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'correct_label.npy')).tolist()
    # correct_name = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'correct_name.npy')).tolist()
    # wrong_sameParent_rel_label = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_sameParent_rel_label.npy')).tolist()
    # wrong_sameParent_name = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_sameParent_name.npy')).tolist()
    # wrong_diffParent_rel_label = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_diffParent_rel_label.npy')).tolist()
    # wrong_diffParent_name = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_diffParent_name.npy')).tolist()

    # out_path = os.path.join(dataset_path, 'ImageNet_Val', 'task2_info', f'model.{exampleModel}')
    # os.makedirs(out_path, exist_ok=True)

    # for input_label in (range(1000)):
    #     wrong_diff = []
    #     wrong_same = []
    #     corr_name = []
    #     for i in range(len(wrong_diffParent_rel_label)):
    #         if wrong_diffParent_rel_label[i] == input_label:
    #             wrong_diff.append(wrong_diffParent_name[i])
    #     for i in range(len(wrong_sameParent_rel_label)):
    #         if wrong_sameParent_rel_label[i] == input_label:
    #             wrong_same.append(wrong_sameParent_name[i])
    #     for i in range(len(correct_label)):
    #         if correct_label[i] == input_label:
    #             corr_name.append(correct_name[i])
    #     if accuracy[input_label] == 100:
    #         np.save(os.path.join(out_path, f'label_{input_label}_correct_name.npy'), corr_name)
    #     else:
    #         np.save(os.path.join(out_path, f'label_{input_label}_correct_name.npy'), corr_name)
    #         np.save(os.path.join(out_path, f'label_{input_label}_wrong_same_name.npy'), wrong_same)
    #         np.save(os.path.join(out_path, f'label_{input_label}_wrong_diff_name.npy'), wrong_diff)


def getCorrect(model_list, dataset_path, input_label):
    correct_lists = ()
    for i in range(len(model_list)):
        model_name = model_list[i]
        correct_img = np.load(os.path.join(
            dataset_path, 'ImageNet_Val', f'model.{model_name}', 'correct_idx.npy'))
        correct_lists += (correct_img,)
    img_idx_list = reduce(np.intersect1d, correct_lists)

    index_list = np.load(os.path.join(dataset_path, 'index.npy'))
    label_list = np.load(os.path.join(dataset_path, 'label.npy'))
    name_list = np.load(os.path.join(dataset_path, 'name.npy'))

    img_name_list = []
    if input_label == None:
        for i in range(label_list.shape[0]):
            if index_list[i] in img_idx_list:
                img_name_list.append(name_list[i])
    else:
        for i in range(label_list.shape[0]):
            if index_list[i] in img_idx_list and label_list[i] == input_label and len(img_name_list) < 20:
                img_name_list.append(name_list[i])

    return img_name_list


def getRandom(dataset_path, input_label):
    label_list = np.load(os.path.join(dataset_path, 'label.npy')).tolist()
    img_list = np.load(os.path.join(dataset_path, 'name.npy')).tolist()
    full_index_list = []
    for i in range(len(label_list)):
        if label_list[i] == input_label:
            full_index_list.append(i)

    random.seed(10)
    index_list = random.sample(full_index_list, 20)
    index_list.sort()
    img_name_list = []
    for idx in index_list:
        img_name_list.append(img_list[idx])
    return img_name_list


def ssim(imageA, imageB):
    # compare image similarity by mse
    imageA = np.array(imageA)
    imageB = np.array(imageB)

    score = compare_ssim(imageA, imageB, multichannel=True)
    # range: [-1, 1], smaller score means higher similarity
    return score


def mse(imageA, imageB):
    # compare image similarity by mse
    imageA = np.array(imageA)
    imageB = np.array(imageB)

    score = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    score /= float(imageA.shape[0] * imageA.shape[1])
    # smaller score means higher similarity
    return score


def l1(imageA, imageB):
    # compare image similarity by mse
    imageA = np.array(imageA)
    imageB = np.array(imageB)

    score = np.sum(np.abs(imageA.astype("float") - imageB.astype("float")))
    score /= float(imageA.shape[0] * imageA.shape[1])
    # smaller score means higher similarity
    return score


def hashed(imageA, imageB):
    # compare image similarity by ImageHash
    hash_1 = imagehash.average_hash(imageA)
    hash_2 = imagehash.average_hash(imageB)
    score = float(abs(hash_1 - hash_2))
    # smaller score means higher similarity
    return score


def getSimMatrix(output_dir, model_list, exp_name, compRule, dataset_path):
    cor_path = os.path.join(dataset_path, 'ImageNet_Val',
                            'task1_info', 'corr_matrix.png')
    img_list = []
    for model_name in model_list:
        exp_res = Image.open(os.path.join(
            output_dir, f'{model_name}_{exp_name}.png')).convert('RGB').resize((224, 224))
        img_list.append(exp_res)

    distance = np.zeros((len(model_list), len(model_list)))
    for iii in range(len(model_list)):
        for jjj in range(len(model_list)):
            img = img_list[iii]
            comp_img = img_list[jjj]
            if compRule == 'hashed':
                sim_score = hashed(img, comp_img)
                # sim_score = exp(-dis_score)
            elif compRule == 'mse':
                sim_score = mse(img, comp_img)
                # sim_score = exp(-dis_score)
            elif compRule == 'l1':
                sim_score = l1(img, comp_img)
                # sim_score = exp(-dis_score)
            elif compRule == 'ssim':
                sim_score = ssim(img, comp_img)
            else:
                print('comp rule name wrong!')
            distance[iii, jjj] = sim_score

    if compRule != 'ssim':
        sim_distance = 2 / np.max(distance) * distance * -1 + 1
    else:
        sim_distance = distance
        
    distance_df = DataFrame(sim_distance, index=model_list, columns=model_list)
    plt.figure()
    sns.set()
    ax = sns.heatmap(
        distance_df,
        # vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        # square=True
    )
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right'
    )
    # ax.set_xticks([])
    # ax.set_yticks([])
    plt.savefig(cor_path, bbox_inches='tight')
    plt.close()
    # print(compRule, 'score: ', np.max(distance), np.min(distance))
    return cor_path


def comp(vis_method, sim_stand, model_list, base_name, output_dir):
    img_list = []
    for model_name in model_list:
        if vis_method == 'Grad-CAM':
            exp_res = Image.open(os.path.join(
                output_dir, f'{model_name}_gradcam.JPEG')).convert('RGB').resize((224, 224))
        elif vis_method == 'Grad-CAM++':
            exp_res = Image.open(os.path.join(
                output_dir, f'{model_name}_gradcampp.JPEG')).convert('RGB').resize((224, 224))
        img_list.append(exp_res)

    distance = np.zeros((len(model_list), len(model_list)))
    find_min = np.zeros((len(model_list), len(model_list)))
    for iii in range(len(model_list)):
        for jjj in range(len(model_list)):
            img = img_list[iii]
            comp_img = img_list[jjj]
            if sim_stand == 'hashed':
                sim_score = hashed(img, comp_img)
                # sim_score2 = hashed(comp_img, img)
            elif sim_stand == 'mse':
                sim_score = mse(img, comp_img)
                # sim_score2 = mse(comp_img, img)
            elif sim_stand == 'l1':
                sim_score = l1(img, comp_img)
                # sim_score2 = l1(comp_img, img)
            elif sim_stand == 'ssim':
                sim_score = 1 - ssim(img, comp_img)
                # sim_score2 = ssim(comp_img, img)

            # if sim_score == sim_score2:
            #     print('right!', sim_stand, iii, jjj)
            # else:
                # print('wrong!', sim_stand, iii, jjj, sim_score, sim_score2)
            distance[iii, jjj] = sim_score
            find_min[iii, jjj] = sim_score

    # print(model_list)

    # # distance
    unsim_tup = np.where(distance == np.max(distance))
    for k in range(len(model_list)):
        find_min[k, k] = float('inf')
    sim_tup = np.where(find_min == np.min(find_min))
    print('most unsimilar, score: ', np.max(distance), np.min(distance))
    print('most similar, score: ', np.min(find_min))
    # print(unsim_tup)
    # print(sim_tup)
    unsim_model = []
    sim_model = []
    for ii in range(len(unsim_tup[0])):
        unsim_1 = unsim_tup[0][ii]
        unsim_2 = unsim_tup[1][ii]
        if model_list[unsim_1] not in unsim_model:
            unsim_model.append(model_list[unsim_1])
        if model_list[unsim_2] not in unsim_model:
            unsim_model.append(model_list[unsim_2])
    for jj in range(len(sim_tup[0])):
        sim_1 = sim_tup[0][jj]
        sim_2 = sim_tup[1][jj]
        if model_list[sim_1] not in sim_model:
            sim_model.append(model_list[sim_1])
        if model_list[sim_2] not in sim_model:
            sim_model.append(model_list[sim_2])

    str_unsim = ','.join(unsim_model)
    str_sim = ','.join(sim_model)
    distance = normalize(distance)
    numpy_dis = {'distance': distance}
    encodedNumpyData = json.dumps(numpy_dis, cls=NumpyArrayEncoder)
    # print(encodedNumpyData)
    # print(str_unsim)
    # print(str_sim)
    message = f'{str_unsim}***{str_sim}***{encodedNumpyData}'

    # tsne_model = manifold.TSNE(n_components=2, random_state=0, metric='precomputed')
    # coords = tsne_model.fit_transform(distance)
    # print(type(coords))
    # print(coords)

    # # cmap = plt.get_cmap('Set1')
    # cmap = plt.get_cmap('Paired')
    # colors = [cmap(i) for i in np.linspace(0, 1, len(model_list))]
    # plt.figure(figsize=(8, 7))
    # plt.scatter(coords[:, 0], coords[:, 1], marker='o', c=colors, s=50, edgecolor='None')
    # markers = []
    # labels = model_list
    # for i in range(len(model_list)):
    #     markers.append(Line2D([0], [0], linestyle='None', marker="o", markersize=10, markeredgecolor="none", markerfacecolor=colors[i]))
    # plt.legend(markers, labels, numpoints=1, bbox_to_anchor=(1.17, 0.5))
    # plt.tight_layout()
    # plt.axis('equal')
    # plt.savefig('1.png')
    # plt.show()
    # print(message)
    return message


def get1000Distance(dataset_path, model_name, rel_label):
    distance_total = np.zeros((1000, 1000))
    distance_count = np.zeros((1000, 1000))
    # prd_label = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'predicted.npy')).tolist()
    certainty_info = np.load(os.path.join(
        dataset_path, 'ImageNet_Val', f'model.{model_name}', 'predicted_certainty.npy'))
    for i in range(len(rel_label)):
        print(f'{i}/50000')
        rL = int(rel_label[i])
        # pL = int(prd_label[i])
        certainty = certainty_info[i]
        for j in range(certainty.shape[0]):
            if j != rL:
                distance_total[rL, j] += (1 - certainty[j])
                distance_count[rL, j] += 1
    print(distance_count)
    distance = np.true_divide(distance_total, distance_count)
    np.save(os.path.join(dataset_path, 'ImageNet_Val',
                         f'model.{model_name}', 'distance_matrix.npy'), distance)


def getDistance(dataset_path, model_name):
    distance = np.load(os.path.join(dataset_path, 'ImageNet_Val',
                                    f'model.{model_name}', 'distance_matrix.npy'))
    for i in range(distance.shape[0]):
        for j in range(distance.shape[1]):
            if i == j:
                distance[i, j] = 0.
    np.save(os.path.join(dataset_path, 'ImageNet_Val',
                         f'model.{model_name}', 'distance_matrix.npy'), distance)
    distance_T = distance.T
    rel_dis = (distance + distance_T) / 2.
    np.save(os.path.join(dataset_path, 'ImageNet_Val',
                         f'model.{model_name}', 'distance_matrix_c.npy'), rel_dis)
    print('done', model_name)


def getScatter(dataset_path, model_name):
    tree_roots = ['n00015388', 'n00021939', 'MISC', 'n00019128',
                  'n09287968', 'n00007846', 'n00017222', 'n12992868']
    grand_name = ['animal', 'artifact', 'MISC', 'natural object',
                  'geological formation', 'person', 'plant', 'fungus']
    grand_info = np.load(os.path.join(
        dataset_path, 'total1000_grandID.npy')).tolist()
    distance = np.load(os.path.join(dataset_path, 'ImageNet_Val',
                                    f'model.{model_name}', 'distance_matrix_c.npy'))

    # set_name = 14
    # for lr in [600, 800, 1000]:
    #     for perplex in [5, 10]:
    # distance = normalize(distance)
    set_name = 666
    out_path = os.path.join('sim_scatter', f'set{set_name}')
    os.makedirs(out_path, exist_ok=True)
    perplex = 5
    lr = 800
    if model_name == 'mobilenet_v2':
        with open(os.path.join('sim_scatter', 'info.txt'), 'a') as f:
            f.write(f'{set_name}\tn_components=2, perplexity={perplex}, early_exaggeration=25, learning_rate={lr}, init=\'random\', random_state=2000, metric=\'precomputed\', verbose=1\n')
    tsne_model = manifold.TSNE(
        n_components=2, perplexity=perplex, early_exaggeration=25, learning_rate=lr, init='random', random_state=2000, metric='precomputed', verbose=1)
    coords = tsne_model.fit_transform(distance)

    # print(type(coords))
    # print(coords.shape)
    # print(coords)
    np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'scatterCoords.npy'), coords)
    # coords_norm = (coords - coords.min(0)) / (coords.max(0) - coords.min(0))

    cmap = plt.get_cmap('Paired')
    c = [cmap(i) for i in np.linspace(0, 1, len(tree_roots))]
    # print(c)
    colors = []
    for i in range(len(grand_info)):
        colors.append(c[tree_roots.index(grand_info[i])])

    plt.figure()
    plt.scatter(coords[:, 0], coords[:, 1],
                marker='o', c=colors, edgecolor='None')

    markers = []
    labels = grand_name
    for i in range(len(tree_roots)):
        markers.append(Line2D([0], [0], linestyle='None', marker="o",
                            markersize=10, markeredgecolor="none", markerfacecolor=c[i]))
    plt.legend(markers, labels, numpoints=1, bbox_to_anchor=(1.17, 0.5))

    plt.tight_layout()
    plt.axis('off')
    plt.savefig(os.path.join(out_path, f'{model_name}.png'))
    plt.close()

def getRGBhist(dataset_path, img_name, output_path, rgb_path, task2_model, exp_name3):
    base_name = os.path.splitext(img_name)[0]
    read_path = os.path.join(output_path, base_name)
    hist_name = exp_name3.split('_')[0]
    hist_path = os.path.join(read_path, f'{task2_model}_{hist_name}_RGBhist.png')
    if os.path.exists(hist_path):
        return hist_path
    else:
        write_path = os.path.join(rgb_path, base_name, hist_name)
        os.makedirs(write_path, exist_ok=True)

        img_path = os.path.join(dataset_path, 'ILSVRC2012_img_val', img_name)
        image = Image.open(img_path).convert('RGB').resize((224, 224))
        img = np.array(image)
        exp_path = os.path.join(read_path, f'{task2_model}_{exp_name3}.npy')
        exp_res = np.load(exp_path)/255.
        idx_list = []
        for i in range(exp_res.shape[0]):
            for j in range(exp_res.shape[1]):
                mask_value = exp_res[i, j]
                if mask_value < 0.5:
                    img[i, j, 0] = 0
                    img[i, j, 1] = 0
                    img[i, j, 2] = 0
                    cur_idx = [i, j]
                    idx_list.append(cur_idx)
        im = Image.fromarray(img)
        im.save(os.path.join(write_path, 'masked.png'))
        np.save(os.path.join(write_path, 'filterout.npy'), idx_list)
        R_channel = []
        G_channel = []
        B_channel = []
        for i in range(224):
            for j in range(224):
                if [i, j] not in idx_list:
                    R_channel.append(img[i, j, 0])
                    G_channel.append(img[i, j, 1])
                    B_channel.append(img[i, j, 2])
        np.save(os.path.join(write_path, 'R_channel.npy'), R_channel)
        np.save(os.path.join(write_path, 'G_channel.npy'), G_channel)
        np.save(os.path.join(write_path, 'B_channel.npy'), B_channel)
        plt.figure(img_name + 'hist')
        _ = plt.hist(R_channel, bins = 256, color = 'red', alpha = 0.5)
        _ = plt.hist(G_channel, bins = 256, color = 'Green', alpha = 0.5)
        _ = plt.hist(B_channel, bins = 256, color = 'Blue', alpha = 0.5)
        _ = plt.xlabel('Intensity Value')
        _ = plt.ylabel('Count')
        _ = plt.legend(['Red_Channel', 'Green_Channel', 'Blue_Channel'])
        plt.savefig(hist_path)
        plt.close()
        return hist_path
