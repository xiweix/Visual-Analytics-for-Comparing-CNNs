import os
import csv
import numpy as np
import pandas as pd
import random
from utils import *
from collections import Counter
from scipy import stats
from functools import reduce
# import random
from random import choice, shuffle, sample
from scorecam_main import scorecamMain
from gradcam_main import gradcamMain
from scorecam_utils import scorecam_to_img
from gradcam_utils import cam_to_img
from smoothgradcam_main import smooth_main
from BBMP import BBMP_process

dataset_path = os.path.join(os.path.dirname(
    os.path.dirname(os.getcwd())), 'dataset')
output_path = os.path.join(os.path.dirname(
    os.path.dirname(os.getcwd())), 'exp_out')
os.makedirs(output_path, exist_ok=True)
total_img = np.load(os.path.join(dataset_path, 'name.npy')).tolist()
full_model_list = [
    'mobilenet_v2',
    'alexnet',
    'resnet18',
    'resnet34',
    'resnet50',
    'resnet101',
    'resnet152',
    'densenet121',
    'densenet161',
    'densenet169',
    'densenet201',
    'squeezenet1_1',
    'shufflenet_v2_x0_5'
]
full_model_acc = [
    71.878,
    56.522,
    69.758,
    73.314,
    76.13,
    77.374,
    78.312,
    74.434,
    77.138,
    75.6,
    76.894,
    58.178,
    60.552
]
full_model_param = [
    2225153,
    57007937,
    11177025,
    21285185,
    23510081,
    42502209,
    58145857,
    6954881,
    26474209,
    12486145,
    18094849,
    723009,
    342817
]

# # generate vis results for main page
# for exampleModel in full_model_list:
#     example_names = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'example_names.npy')).tolist()
#     # gradcamMain([exampleModel], example_names, dataset_path, output_path)
#     # scorecamMain([exampleModel], example_names, dataset_path, output_path)
#     smooth_main(dataset_path, example_names, [exampleModel], output_path)
#     # for img_name in example_names:
#     #     BBMP_process(dataset_path, img_name, exampleModel, output_path)
#     print('finish: ', exampleModel)

# # generate vis results for task1
# label_list = list(range(0, 30))
# example_names = []
# for input_label in label_list:
#     names = np.load(os.path.join(dataset_path, 'ImageNet_Val', 'task1_info',
#                                  f'label_{input_label}_task1examplename.npy')).tolist()
#     example_names.extend(names)
# # scorecamMain(full_model_list, example_names, dataset_path, output_path)
# gradcamMain(['alexnet'], example_names, dataset_path, output_path)
gradcamMain(full_model_list, total_img, dataset_path, output_path)

# i = 0
# for img_name in example_names:
#     for model_name in full_model_list:
#         BBMP_process(dataset_path, img_name, model_name, output_path)
#     i += 1
#     print(f'BBMP: {img_name}: {i}/{len(example_names)}')

# # # generate vis results for task2
# for exampleModel in full_model_list:
#     out_path = os.path.join(dataset_path, 'ImageNet_Val', 'task2_info', f'model.{exampleModel}')
#     example_names = np.load(os.path.join(out_path, 'task2examplenameTotal.npy')).tolist()
#     # gradcamMain([exampleModel], example_names, dataset_path, output_path)
#     # smooth_main(dataset_path, example_names, [exampleModel], output_path)
#     i = 0
#     for img_name in example_names:
#         BBMP_process(dataset_path, img_name, exampleModel, output_path)
#         i += 1
#         print(f'{exampleModel} BBMP: {img_name}: {i}/{len(example_names)}')


# acc_0 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[0]}', 'accuracy.npy')).tolist()
# print(type(acc_0[100]))
# print(acc_0[100])


# rel_label = np.load(os.path.join(dataset_path, 'label.npy')).tolist()
# for model_name in full_model_list:
#     print(model_name)
#     get1000Scatter(dataset_path, model_name, rel_label)


# model_name = 'mobilenet_v2'
# certainty = np.load(os.path.join(os.path.dirname(
#     os.path.dirname(os.getcwd())), 'ImageNet_Val', f'model.{model_name}', 'out_certainty.npy'))
# for i in range(certainty.shape[0]):
#     img_certainty = certainty[i, :]

#     print(img_certainty.sum())


# grand_name = np.load(os.path.join(dataset_path, 'grandParent_name.npy')).tolist()
# curLabelName = []
# for curWordID in grand_name:
#     if curWordID == 'MISC':
#         curLabelName.append('MISC')
#     else:
#         curLabelName.append(IDToWord(dataset_path, curWordID))
# print(curLabelName)
# total_id = np.load(os.path.join(dataset_path, 'total1579_ID.npy')).tolist()
# name = total_id[1571:1579]
# for model_name in full_model_list:
#     total_acc = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'total_11579_accuracy.npy')).tolist()
#     name_acc = total_acc[1571:1579]
#     # print(len(total_id), len(total_acc))
#     # print(name)
#     print(name_acc)
#     print(model_name)
#     print(min(name_acc))
#     print(max(name_acc))
#     print('\n\n')

# name = np.load(os.path.join(dataset_path, 'grandParent_name.npy')).tolist()
# print(name)
# name_list = []
# for n in name:
#     if n != 'MISC':
#         name_list.append(IDToWord(dataset_path, n))
#     else:
#         name_list.append('MISC')
# print(name_list)
# for model_name in full_model_list:
#     acc = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'grand8_accuracy.npy')).tolist()
#     print(model_name)
#     print(acc)

# tree_roots = ['n00007846', 'n00015388', 'n00017222', 'n00019128', 'n00021939', 'n00523513', 'n09287968', 'n12992868']
# root0 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[0]}.npy')).tolist()
# root1 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[1]}.npy')).tolist()
# root2 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[2]}.npy')).tolist()
# root3 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[3]}.npy')).tolist()
# root4 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[4]}.npy')).tolist()
# root5 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[5]}.npy')).tolist()
# root6 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[6]}.npy')).tolist()
# root7 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[7]}.npy')).tolist()
# combo = root0 + root1 + root2 + root3 + root4 + root5 + root6 + root7
# for label in range(1000):
#     labelID = idxToID(dataset_path, label)
#     count0 = 0
#     count1 = 0
#     count2 = 0
#     count3 = 0
#     count4 = 0
#     count5 = 0
#     count6 = 0
#     count7 = 0
#     count8 = 0
#     if labelID in combo:
#         if labelID in root0:
#             count0 += 1
#         if labelID in root1:
#             count1 += 1
#         if labelID in root2:
#             count2 += 1
#         if labelID in root3:
#             count3 += 1
#         if labelID in root4:
#             count4 += 1
#         if labelID in root5:
#             count5 += 1
#         if labelID in root6:
#             count6 += 1
#         if labelID in root7:
#             count7 += 1
#     else:
#         count8 += 1
#     total_count = count0 + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8
#     if total_count > 1:
#         print(label, labelID, '---', count0, count1, count2, count3, count4, count5, count6, count7, count8)

# tree_roots = ['n00015388', 'n00021939', 'MISC', 'n00019128', 'n09287968', 'n00007846', 'n00017222', 'n12992868']
# root0 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[0]}.npy')).tolist()
# root1 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[1]}.npy')).tolist()
# root2 = []
# root3 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[3]}.npy')).tolist()
# root4 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[4]}.npy')).tolist()
# root5 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[5]}.npy')).tolist()
# root6 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[6]}.npy')).tolist()
# root7 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[7]}.npy')).tolist()
# count0 = 0
# count1 = 0
# count2 = 0
# count3 = 0
# count4 = 0
# count5 = 0
# count6 = 0
# count7 = 0
# root_name = []
# for name in tree_roots:
#     if name != 'MISC':
#         root_name.append(IDToWord(dataset_path, name))
#     else: root_name.append('MISC')
# print(root_name)
# combo = root0 + root1 + root3 + root4 + root5 + root6 + root7
# for label in range(1000):
#     labelID = idxToID(dataset_path, label)
#     if labelID in combo:
#         if labelID in root0:
#             count0 += 1
#         if labelID in root1:
#             count1 += 1
#         if labelID in root3:
#             count3 += 1
#         if labelID in root4:
#             count4 += 1
#         if labelID in root5:
#             count5 += 1
#         if labelID in root6:
#             count6 += 1
#         if labelID in root7:
#             count7 += 1
#     else:
#         count2 += 1
# total_count = count0 + count1 + count2 + count3 + count4 + count5 + count6 + count7

# print(count0, count1, count2, count3, count4, count5, count6, count7)
# print(total_count)


# tree_roots = ['n00007846', 'n00015388', 'n00017222', 'n00019128', 'n00021939', 'n00523513', 'n09287968', 'n12992868']
# root0 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[0]}.npy')).tolist()
# root1 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[1]}.npy')).tolist()
# root2 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[2]}.npy')).tolist()
# root3 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[3]}.npy')).tolist()
# root4 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[4]}.npy')).tolist()
# root5 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[5]}.npy')).tolist()
# root6 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[6]}.npy')).tolist()
# root7 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[7]}.npy')).tolist()
# combo = root0 + root1 + root2 + root3 + root4 + root5 + root6 + root7
# count0 = 0
# count1 = 0
# count2 = 0
# count3 = 0
# count4 = 0
# count5 = 0
# count6 = 0
# count7 = 0
# count8 = 0

# father_label_list = []
# for label in range(1000):
#     labelID = idxToID(dataset_path, label)
#     father_label = findParentLabel(dataset_path, labelID)
#     for father in father_label:
#         if father not in father_label_list:
#             father_label_list.append(father)
# print(len(father_label_list))
# for labelID in father_label_list:
#     if labelID in combo:
#         if labelID in root0:
#             count0 += 1
#         if labelID in root1:
#             count1 += 1
#         if labelID in root2:
#             count2 += 1
#         if labelID in root3:
#             count3 += 1
#         if labelID in root4:
#             count4 += 1
#         if labelID in root5:
#             count5 += 1
#         if labelID in root6:
#             count6 += 1
#         if labelID in root7:
#             count7 += 1
#     else:
#         count8 += 1
# total_count = count0 + count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8

# print(total_count, count0, count1, count2, count3, count4, count5, count6, count7, count8)

# # father label number: 578
# father_label_list = []
# for label in range(1000):
#     labelID = idxToID(dataset_path, label)
#     father_label = findParentLabel(dataset_path, labelID)
#     for father in father_label:
#         father_label_content = IDToWord(dataset_path, father)
#         if '\'s' in father_label_content:
#             print(father_label_content)
#             father_label_content = father_label_content.replace('\'s', ' s')
#             print(father_label_content)
#         elif '\'' in father_label_content:
#             print(father_label_content)
#             father_label_content = father_label_content.replace('\'', '')
#             print(father_label_content)
#         if father_label_content not in father_label_list:
#             father_label_list.append(father_label_content)
# print(len(father_label_list))
# np.save('parent_name.npy', father_label_list)


# write_path = "parentWordToGrad.txt"
# with open(write_path, 'a') as ftxt:
#     ftxt.write('{\n')
# for father_content in father_label_list:
#     with open(write_path, 'a') as ftxt:
#         ftxt.write(f'\"{father_content}\": [\"\"],\n')
# with open(write_path, 'a') as ftxt:
#     ftxt.write('}\n')


# for task1
# label_list = list(range(0, 500))
# for input_label in label_list:
#     task1ImgSelection(dataset_path, input_label)


# statistic analysis
# csv_path = os.path.join(dataset_path, 'ImageNet_Val', 'accuracy_analysis1.csv')
# new_csv_path = os.path.join(dataset_path, 'ImageNet_Val', 'accuracy_analysis2.csv')
# new_csv_path2 = os.path.join(dataset_path, 'ImageNet_Val', 'accuracy_analysis3.csv')
# with open(csv_path, 'r') as fcsv:
#     prj_info = csv.reader(fcsv)
#     for line in prj_info:
#         if prj_info.line_num == 1:
#             name_list = line
#             line.extend(name_list)
#             line.append('max')
#             line.append('min')
#             line.append('max_min')
#             line.append('mean')
#             line.append('median')
#             line.append('mode')
#             with open(new_csv_path, 'a') as f:
#                 writer = csv.writer(f)
#                 writer.writerow(line)
#         elif prj_info.line_num == 1002:
#             labelAccuracy = []
#             for ii in range(len(line)):
#                 labelAccuracy.append(float("%.3f" % float(line[ii])))
#             sort_labelAccuracy_idx_list = np.argsort(labelAccuracy)
#             order_list = [0 for i in range(len(full_model_list))]
#             i = 0
#             for idx in sort_labelAccuracy_idx_list:
#                 order_list[idx] = i
#                 i += 1
#             print(name_list)
#             print(order_list)

#             line.extend(order_list)
#             line.append(max(labelAccuracy))
#             line.append(min(labelAccuracy))
#             line.append(max(labelAccuracy) - min(labelAccuracy))
#             line.append(np.mean(labelAccuracy))
#             line.append(np.median(labelAccuracy))
#             line.append(stats.mode(labelAccuracy)[0][0])
#             with open(new_csv_path, 'a') as f:
#                 writer = csv.writer(f)
#                 writer.writerow(line)
#         else:
#             print('wrong')
# df = pd.read_csv(new_csv_path)
# df.values
# data = df.as_matrix()
# data = list(map(list,zip(*data)))
# data = pd.DataFrame(data)
# data.to_csv(new_csv_path2, header=0, index=0)

# with open(new_csv_path2, 'r') as fcsv:
#     prj_info = csv.reader(fcsv)
#     for line in prj_info:
#         if prj_info.line_num == 15:
#             count_number = []
#             for i in range(len(line)):
#                 # print(l)
#                 l = line[i]
#                 if float(l) >= 7:
#                     print(i, l)
#                 count_number.append(float(l))
#             print('ALex', Counter(count_number))
#         elif prj_info.line_num == 20:
#             count_number = []
#             for i in range(len(line)):
#                 # print(l)
#                 l = line[i]
#                 if float(l) <= 4:
#                     print(i, l)
#                 count_number.append(float(l))
#             print('res152', Counter(count_number))
#             print(len(line))



            
# for exampleModel in full_model_list:
# smooth_main(dataset_path, example_names, full_model_list, output_path)
# task1ImgGeneration(full_model_list, dataset_path)

# out_path = os.path.join(dataset_path, 'ImageNet_Val', 'task1_info')
# label_list = np.load(os.path.join(dataset_path, 'label.npy')).tolist()
# name_list = np.load(os.path.join(dataset_path, 'name.npy')).tolist()
# all_correct = np.load(os.path.join(out_path, 'total_allcorrect.npy')).tolist()
# all_wrong = np.load(os.path.join(out_path, 'total_allwrong.npy')).tolist()
# all_both = np.load(os.path.join(out_path, 'total_correctandwrong.npy')).tolist()
# task1ImgGet(out_path, label_list, name_list, all_correct, all_wrong, all_both)


# for task2
# label_list = list(range(1000))
# for exampleModel in full_model_list:
#     print(exampleModel)
#     task2ImgGet(dataset_path, exampleModel)


# label_list = list(range(1000))
# # task1ImgSelection(full_model_list, dataset_path)
# for input_label in label_list:
#     task1ImgSelection(dataset_path, input_label)
# for exampleModel in full_model_list:
# # exampleModel = full_model_list[2]
# # label_list = list(range(200))
# # example_names, _, _, _, _ = getMultiClassInfo(dataset_path, exampleModel, label_list)
#     example_names = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'example_names.npy')).tolist()
#     print(len(example_names))
#     scorecamMain([exampleModel], example_names, dataset_path, output_path)
#     # i = 0
#     for image_name in example_names:
#         BBMP_process(dataset_path, image_name, exampleModel, output_path)
#         # smooth_main(dataset_path, image_name, exampleModel, output_path)
#     #     i += 1
#     #     print(f'{image_name}\t{i}/{len(example_names)}')


# for exampleModel in full_model_list:
# exampleModel = full_model_list[2]
# label_list = list(range(1000))
# example_names, _, _, _, _ = getMultiClassInfo(dataset_path, exampleModel, label_list)
# print(len(example_names))
# scorecamMain([exampleModel], example_names, dataset_path, output_path)
# print('finish scorecamMain')
# gradcamMain([exampleModel], example_names, dataset_path, output_path)
# print('finish gradcamMain')
#     correct_count = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'correct_count.npy')).tolist()
#     wrong_sameParent_count = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_sameParent_count.npy')).tolist()
#     wrong_diffParent_count = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'wrong_diffParent_count.npy')).tolist()
#     label_list = []
#     for i in range(1000):
#         if wrong_diffParent_count[i] != 0 and wrong_sameParent_count[i] != 0 and correct_count[i] != 0:
#             label_list.append(i)
#     np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'unempty_labels.npy'), label_list)

# unempty_lists = ()
# for i in range(len(full_model_list)):
#     model_name = full_model_list[i]
#     unempty_labels = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'unempty_labels.npy'))
#     unempty_lists += (unempty_labels,)
# unempty_label_list = reduce(np.intersect1d, unempty_lists)
# print(len(unempty_label_list))
# np.save(os.path.join(dataset_path, 'ImageNet_Val', 'unempty_labels.npy'), unempty_label_list)

# label_num = 3
# random.seed(1)
# labels = sample(label_list, label_num)

# example_names, example_rel, example_acc, example_prd, example_certainty = getMultiClassInfo(dataset_path, exampleModel, label_list)
# print(exampleModel)
# scorecamMain([exampleModel], example_names, dataset_path, output_path)
# print('finish scorecamMain')
# gradcamMain([exampleModel], example_names, dataset_path, output_path)
# print('finish gradcamMain')
# np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'example_names.npy'), example_names)
# np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'example_rel_label.npy'), example_rel)
# np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'example_acc.npy'), example_acc)
# np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'example_prd_label.npy'), example_prd)
# np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'example_certainty.npy'), example_certainty)

# gradcamMain([exampleModel], example_names, dataset_path, output_path)
# scorecamMain([exampleModel], example_names, dataset_path, output_path)
# for image_name in example_names:
#     scorecam_to_img(dataset_path, image_name, exampleModel, output_path)
# print(len(example_names))
# print(len(example_rel))
# print(len(example_acc))
# print(len(example_prd))
# print(len(example_certainty))
# print(example_rel)
# print(example_prd)

# correct_label = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'correct_label.npy')).tolist()
# correct_count = list(0 for i in range(1000))
# for l in correct_label:
#     correct_count[l] += 1
# print(len(correct_label))
# print(sum(correct_count))
# np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'correct_count.npy'), correct_count)
# print(exampleModel)
# processWrong(exampleModel, dataset_path)
#   # findCorWro(exampleModel, dataset_path, total_img)
# # exampleModel = full_model_list[2]
#   findLabelAcc(exampleModel, dataset_path)

# with open('IDtoPARENTID.txt', 'a') as ftxt:
#   ftxt.write('{\n')
# for input_label in range(1000):
#     wordID = idxToID(dataset_path, input_label)
#     parentID = findParentLabel(dataset_path, wordID)

#     with open('IDtoPARENTID.txt', 'a') as ftxt:
#       ftxt.write(f'\"{wordID}\": {parentID}, \n')
# with open('IDtoPARENTID.txt', 'a') as ftxt:
#   ftxt.write('}\n')
#     # print(wordID)
