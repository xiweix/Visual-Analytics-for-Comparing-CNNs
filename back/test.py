import os
import numpy as np
# import click
# from gradcam_main import *
# from multi_grad_main import *
# from utils import getScatter, getDistance
# from functools import reduce
# import torchvision.models as models
# from BBMP import *
import cv2
import torch
from smoothgradcam_main2 import smooth_main
from PIL import Image
# from collections import Counter

dataset_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'dataset')
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
output_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'test_vis')
img_list = ['ILSVRC2012_val_00001571.JPEG', 'ILSVRC2012_val_00002597.JPEG', 'ILSVRC2012_val_00034058.JPEG', 'ILSVRC2012_val_00038798.JPEG', 'ILSVRC2012_val_00005918.JPEG']
model_name = 'resnet152'
# model_list = ['resnet152ly40', 'resnet152ly41', 'resnet152ly42', 'resnet152ly30', 'resnet152ly31', 'resnet152ly32', 'resnet152ly33', 'resnet152ly34', 'resnet152ly35', 'resnet152ly36', 'resnet152ly37', 'resnet152ly38', 'resnet152ly39', 'resnet152ly310']
# smooth_main(dataset_path, [img_list[0]], model_list, output_path)
# smooth_main(dataset_path, img_list[0], model_name, output_path)

base_name = os.path.splitext(img_list[0])[0]
output_dir = os.path.join(output_path, base_name)
# # mask0 = np.load(os.path.join(output_dir, f'{model_name}_smoothgradcampp_cam0_ly3.npy'))
# # mask1 = np.load(os.path.join(output_dir, f'{model_name}_smoothgradcampp_cam_ly3.npy'))
# # mask_list = []
# # mask_list.append(np.load(os.path.join(output_dir, f'res152_ly0_smoothgradcampp_cam.npy')))
# # for i in range(3):
# #     mask_list.append(np.load(os.path.join(output_dir, f'res152_ly1_{i}_smoothgradcampp_cam.npy')))
# # for i in range(8):
# #     mask_list.append(np.load(os.path.join(output_dir, f'res152_ly2_{i}_smoothgradcampp_cam.npy')))
# # for i in range(36):
# #     mask_list.append(np.load(os.path.join(output_dir, f'res152_ly3_{i}_smoothgradcampp_cam.npy')))
# # for i in range(2):
# #     mask_list.append(np.load(os.path.join(output_dir, f'res152_ly4_{i}_smoothgradcampp_cam.npy')))
# # print('mask_list length, should be 50', len(mask_list))
# compare_mask = np.load(os.path.join(output_dir, 'res152_ly4_2_smoothgradcampp_cam.npy'))
# print(compare_mask.shape)
# print(np.min(compare_mask), np.max(compare_mask))
# sim_record = np.zeros((compare_mask.shape[0], compare_mask.shape[1]))
# for i in range(compare_mask.shape[0]):
#     for j in range(compare_mask.shape[1]):
#         compare_value = compare_mask[i, j]
#         min_v = float('inf')
#         min_i = 0
#         for k in range(len(mask_list)):
#             find_same = 0
#             cur_mask = mask_list[k]
#             cur_value = cur_mask[i, j]
#             diff = abs(compare_value - cur_value)
#             if compare_value == cur_value:
#                 find_same = 1
#                 min_i = k
#                 break
#             else:
#                 if diff < min_v:
#                     min_v = diff
#                     min_i = k
#         sim_record[i, j] = min_i
# np.save(os.path.join(output_dir, 'sim_record.npy'), sim_record)
# print(sim_record)
# print(sim_record.shape)
# print(np.min(sim_record), np.max(sim_record))
# sim_record = np.load(os.path.join(output_dir, 'sim_record.npy'))
# sim_record = sim_record / 49.

# heatmap = cv2.applyColorMap(np.uint8(255*sim_record), cv2.COLORMAP_VIRIDIS)
# heatmap = np.float32(heatmap) / 255
# cv2.imwrite(os.path.join(output_dir, 'sim_record.png'), np.uint8(255*heatmap))

# # sim_record = np.around(sim_record)
# # print(sim_record.shape)
# # print(np.min(sim_record), np.max(sim_record))
# # heatmap = cv2.applyColorMap(sim_record, cv2.COLORMAP_VIRIDIS)
# # heatmap = torch.from_numpy(heatmap.transpose(2, 0, 1))
# # heatmap = heatmap.float() / 255
# # b, g, r = heatmap.split(1)
# # heatmap = torch.cat([r, g, b])
# # save_image(heatmap, os.path.join(output_dir, 'sim_record.png'))

# # for sim in sim_record:
# #     for s in sim:
# #         print(s)

# img_path = os.path.join(output_dir, 'sim_record.png')
# image = Image.open(img_path).convert('RGB').resize((224, 224))
# img = np.array(image)
# smooth_res = np.load(os.path.join(output_dir, 'res152_ly4_2_smoothgradcampp_cam.npy'))/255.
# print(type(sim_record), sim_record.shape, np.min(sim_record), np.max(sim_record))
# print(type(smooth_res), smooth_res.shape, np.min(smooth_res), np.max(smooth_res))
# for i in range(smooth_res.shape[0]):
#     for j in range(smooth_res.shape[1]):
#         mask_value = smooth_res[i, j]
#         if mask_value < 0.5:
#             sim_record[i, j] = 0
# np.save(os.path.join(output_dir, 'masked_sim_record.npy'), sim_record)
# idx_list = []
# for i in range(smooth_res.shape[0]):
#     for j in range(smooth_res.shape[1]):
#         mask_value = smooth_res[i, j]
#         if mask_value < 0.5:
#             # print('before, R: ', type(img[i, j, 0]), img[i, j, 0])
#             # print('before, G: ', type(img[i, j, 1]), img[i, j, 1])
#             # print('before, B: ', type(img[i, j, 1]), img[i, j, 1])
#             img[i, j, 0] = 0
#             img[i, j, 1] = 0
#             img[i, j, 2] = 0
#             cur_idx = [i, j]
#             idx_list.append(cur_idx)
#             # print('after: ', type(img[i, j, 0]), img[i, j, 0])
#             # print('after: ', type(img[i, j, 1]), img[i, j, 1])
#             # print('after: ', type(img[i, j, 2]), img[i, j, 2])
# # print(type(img), img.shape)
# im = Image.fromarray(img)
# im.save(os.path.join(output_dir, 'masked_sim_record.png'))
# np.save(os.path.join(output_dir, 'filterout.npy'), idx_list)

# masked_sim_record = np.load(os.path.join(output_dir, 'masked_sim_record.npy'))
sim_record = np.load(os.path.join(output_dir, 'sim_record.npy'))

smooth_res = np.load(os.path.join(output_dir, 'res152_ly4_2_smoothgradcampp_cam.npy'))/255.
# print(type(masked_sim_record), masked_sim_record.shape, np.min(masked_sim_record), np.max(masked_sim_record))
# print(type(smooth_res), smooth_res.shape, np.min(smooth_res), np.max(smooth_res))

import matplotlib.pyplot as plt

# fig, ax = plt.subplots()
# ax.set_aspect("equal")

# x = list(range(224)) # xdata
# y = list(range(224)) # ydata
# img_path = os.path.join(output_dir, 'sim_record.png')
# image = Image.open(img_path).convert('RGB').resize((224, 224))
# img = np.array(image)
# print(img[3,3,0], type(img[3,3,0]))
# for i in range(224):
#     for j in range(224):
#         img[i, j, 0] = int(smooth_res[i, j] * 255)
#         img[i, j, 1] = 0
#         img[i, j, 2] = int(sim_record[i, j] * 255)
# im = Image.fromarray(img)
# im.save(os.path.join(output_dir, 'sim_record_2dcolormap.png'))

# create a very simple colormap, 
#  mapping parameter 1 to the red channel and 
#          parameter 2 to the blue channel
# colors = []
# for k in range(len(p1)):
#     color = (p1[k], 0., p2[k], 1.)
#     colors.append(color)
# print(colors[5], type(colors[5]))

# cmap = plt.get_cmap('Paired')
# c = [cmap(i) for i in np.linspace(0, 1, 5)]
# print(c[2], type(c[2]))

# cmap = lambda p1,p2 : (p1, 0, p2)
# colors = []
# for i in range(224):
#     colors.append(cmap(p1[i],p2[i]))
# print(type(colors), colors)

# plt.figure()
# plt.scatter(x, y, marker='o', c=colors, edgecolor='None')

# # # markers = []
# # # labels = grand_name
# # # for i in range(len(tree_roots)):
# # #     markers.append(Line2D([0], [0], linestyle='None', marker="o",
# # #                         markersize=10, markeredgecolor="none", markerfacecolor=c[i]))
# # # plt.legend(markers, labels, numpoints=1, bbox_to_anchor=(1.17, 0.5))

# plt.tight_layout()
# plt.axis('off')
# plt.savefig(os.path.join(output_dir, '2dcolormap.png'))
# plt.close()


# # put shapes at positions (x[i], y[i]) and colorize them with our
# # cmap according to their respective parameters
# for i in range(len(x)):
#        circle = plt.Circle((x[i], y[i]), 0.1, color=cmap(p1[i],p2[i]))
#        ax.add_artist(circle)
#     #    tx="p1: {}\np2: {}".format(p1[i],p2[i]) # create a label
#     #    ax.text(x[i], y[i], tx, ha="center", color="w", va="center")

# # ax.set_xlim(0,4)
# # ax.set_ylim(0,4)
# ax.set_xlabel("x")
# ax.set_ylabel("y")

# # create the legend:

# # plt.subplots_adjust(left=0.1, right=0.05, top=0.85)
plt.figure()
cp1 = np.linspace(0,1)
cp2 = np.linspace(0,1)
Cp1, Cp2 = np.meshgrid(cp1,cp2)
C0 = np.zeros_like(Cp1)
# make RGB image, p1 to red channel, p2 to blue channel
Legend = np.dstack((Cp1, C0, Cp2))
# parameters range between 0 and 1
plt.imshow(Legend, origin="lower", extent=[0,1,0,1])
plt.xlabel("Visual Explanation")
plt.ylabel("Layer Contribution")
plt.title("2D cmap legend", fontsize=10)
plt.savefig(os.path.join(output_dir, '2dcolormap_legend.png'))












# print(mask0.shape)
# print(np.min(mask0), np.max(mask0))

# print(mask1.shape)
# print(np.min(mask1), np.max(mask1))

# tree_roots = ['n00015388', 'n00021939', 'MISC', 'n00019128', 'n09287968', 'n00007846', 'n00017222', 'n12992868']
# grand_name = ['animal', 'artifact', 'MISC', 'natural object', 'geological formation', 'person', 'plant', 'fungus']
# root0 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[0]}.npy')).tolist()
# root1 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[1]}.npy')).tolist()
# root2 = []
# root3 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[3]}.npy')).tolist()
# root4 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[4]}.npy')).tolist()
# root5 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[5]}.npy')).tolist()
# root6 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[6]}.npy')).tolist()
# root7 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[7]}.npy')).tolist()
# combo = root0 + root1 + root3 + root4 + root5 + root6 + root7
# label1000_grand = []
# for label in range(1000):
#     labelID = idxToID(dataset_path, label)
#     if labelID in combo:
#         if labelID in root0:
#             label1000_grand.append(tree_roots[0])
#         elif labelID in root1:
#             label1000_grand.append(tree_roots[1])
#         elif labelID in root3:
#             label1000_grand.append(tree_roots[3])
#         elif labelID in root4:
#             label1000_grand.append(tree_roots[4])
#         elif labelID in root5:
#             label1000_grand.append(tree_roots[5])
#         elif labelID in root6:
#             label1000_grand.append(tree_roots[6])
#         elif labelID in root7:
#             label1000_grand.append(tree_roots[7])
#     else:
#         label1000_grand.append(tree_roots[2])
# print(len(label1000_grand))
# np.save(os.path.join(dataset_path, 'total1000_grandID.npy'), label1000_grand)


# rel_label = np.load(os.path.join(dataset_path, 'label.npy')).tolist()
# print(len(rel_label))
# for model_name in full_model_list:
#     print(model_name)
    # get1000Distance(dataset_path, model_name, rel_label)
# for model_name in full_model_list:
#     print(model_name)
#     # getDistance(dataset_path, model_name)
#     getScatter(dataset_path, model_name)

# getDistance(dataset_path, model_name)
    # prd_label = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'predicted.npy')).tolist()

    # certainty = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'predicted_certainty.npy'))
    # print(certainty.shape, type(certainty))
    # print(certainty[0].shape, type(certainty[0]))
    # cet = certainty[0]
    # for k in range(cet.shape[0]):
    #     print(k, cet[k], type(cet[k]))
    # for i in range(len(rel_label)):
    #     print(rel_label[i], type(rel_label[i]))
    #     print(prd_label[i], type(prd_label[i]))


# output_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'vis_out')
# model_list = [
#     'mobilenet_v2',
#     'alexnet',
#     'resnet18',
#     'resnet34',
#     'resnet50',
#     'resnet101',
#     'resnet152',
#     'densenet121',
#     'densenet161',
#     'densenet169',
#     'densenet201',
#     'squeezenet1_1',
#     'shufflenet_v2_x0_5'
# ]
# name_list = np.load(os.path.join(dataset_path, 'name.npy'))
# gradcamMain('Grad-CAM', model_list, name_list, dataset_path, output_path)
# gradcamMain('Grad-CAM++', model_list, name_list, dataset_path, output_path)

# # empty_list_gradcam = []
# # empty_list_gradcampp = []
# # for name in name_list:
# #     for model_name in model_list:
# #         base_name = os.path.splitext(name)[0]
# #         output_dir = os.path.join(output_path, base_name)
# #         if not os.path.exists(os.path.join(output_dir, f'{model_name}_gradcam.JPEG')):
# #             print(f'gradcam wrong! {base_name}')
# #             empty_list_gradcam.append(name)
# #         if not os.path.exists(os.path.join(output_dir, f'{model_name}_gradcampp.JPEG')):
# #             print(f'gradcam++ wrong! {base_name}')
# #             empty_list_gradcampp.append(name)
# # np.save('grad_cam.npy', empty_list_gradcam)
# # np.save('grad_campp.npy', empty_list_gradcampp)


# correct_lists = ()
# for i in range(len(model_list)):
#     model_name = model_list[i]
#     correct_img = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'correct_idx.npy'))
#     correct_lists += (correct_img,)
# img_idx_list = reduce(np.intersect1d, correct_lists)

# index_list = np.load(os.path.join(dataset_path, 'index.npy'))
# label_list = np.load(os.path.join(dataset_path, 'label.npy'))
# name_list = np.load(os.path.join(dataset_path, 'name.npy'))

# print(index_list.shape, label_list.shape, name_list.shape)
# empty_label = []
# for input_label in range(1000):
#     img_name_list = []
#     i = 0
#     select_index = []
#     while i < label_list.shape[0] and len(img_name_list) < 20:
#         if index_list[i] in img_idx_list and label_list[i] == input_label:
#             img_name_list.append(name_list[i])
#             select_index.append(i)
#         i += 1
#     if len(img_name_list) == 0:
#         empty_label.append(input_label)
#         print('empty: ', input_label)
#     else:
#         np.save(os.path.join(dataset_path, 'label_info', f'label_{input_label}_imgname.npy'), img_name_list)
#         for single_model in model_list:
#             probability = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{single_model}', 'probability.npy'))
#             if probability.shape[0] != 50000:
#                 print(input_label, single_model, 'probability size wrong!')
#             a = []
#             for idx in select_index:
#                 a.append(probability[idx])
#             np.save(os.path.join(dataset_path, 'label_info', f'label_{input_label}_prob_{single_model}.npy'), a)
#             if len(img_name_list) != len(a):
#                 print('wrong!')
# print(empty_label)
# print(len(empty_label))

# np.save(os.path.join(dataset_path, 'label_info', 'empty_labels.npy'), empty_label)

# @click.command()
# @click.option('--idx',
#               type=int,
#               default=0,
#               help='model index in the list, range: 0-12')
# @click.option('--minlabel',
#               type=int,
#               default=0,
#               help='min label, range: 0-999 except [638, 664, 744, 782, 818, 836, 848, 885]')
# @click.option('--maxlabel',
#               type=int,
#               default=100,
#               help='max label, range: 0-999 except [638, 664, 744, 782, 818, 836, 848, 885]')
# def main(idx, minlabel, maxlabel):
#     model_lists = [
#         ['mobilenet_v2'],
#         ['alexnet'],
#         ['resnet18'],
#         ['resnet34'],
#         ['resnet50'],
#         ['resnet101'],
#         ['resnet152'],
#         ['densenet121'],
#         ['densenet161'],
#         ['densenet169'],
#         ['densenet201'],
#         ['squeezenet1_1'],
#         ['shufflenet_v2_x0_5']
#     ]
#     dataset_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'dataset')
#     output_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'vis_out')
#     model_list = model_lists[idx]
#     # for label in range(minlabel, maxlabel):
#     #     if label not in [638, 664, 744, 782, 818, 836, 848, 885]:
#     #         image_names = np.load(os.path.join(dataset_path, 'label_info', f'label_{label}_imgname.npy')).tolist()
#     #         demo1(dataset_path, image_names, model_name, output_path, label)
#     #         print(f'finish: {model_name}, label: {label}, {len(image_names)}')
#     for label in [638, 664, 744, 782, 818, 836, 848, 885]:
#         image_names = getCorrect(model_list, dataset_path, label)
#         demo1(dataset_path, image_names, model_list[0], output_path, label)
#         print(f'finish: {model_list[0]}, label: {label}, {len(image_names)}')

# if __name__ == '__main__':
#     main()

# dataset_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'dataset')
# model_name = 'resnet152'
# # accuracy_list = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'accuracy.npy')).tolist()
# # accuracy = '%.2f' % accuracy_list[1000] + '%'
# input_label = 100
# img_name_list = np.load(os.path.join(dataset_path, 'label_info', f'label_{input_label}_imgname.npy')).tolist()
# probability_list = np.load(os.path.join(dataset_path, 'label_info', f'label_{input_label}_prob_{model_name}.npy')).tolist()


# total_prob = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'probability.npy')).tolist()
# total_img = np.load(os.path.join(dataset_path, 'name.npy')).tolist()
# print(len(total_prob))
# print(len(total_img))

# prob_list = []
# for imgname in img_name_list:
#     idx = total_img.index(imgname)
#     prob_list.append(total_prob[idx])

# if len(probability_list) == len(prob_list):
#     for i in range(len(prob_list)):
#         print(probability_list[i], prob_list[i])
#         print('%.10f' % probability_list[i])
# else:
#     print('wrong! size did not match')



# @click.command()
# @click.option('--idx',
#               type=int,
#               default=0,
#               help='model index in the list, range: 0-12')
# @click.option('--minlabel',
#               type=int,
#               default=0,
#               help='min label, range: 0-999 except [638, 664, 744, 782, 818, 836, 848, 885]')
# @click.option('--maxlabel',
#               type=int,
#               default=100,
#               help='max label, range: 0-999 except [638, 664, 744, 782, 818, 836, 848, 885]')
# def main(idx, minlabel, maxlabel):
#     model_list = [
#         'mobilenet_v2',
#         'alexnet',
#         'resnet18',
#         'resnet34',
#         'resnet50',
#         'resnet101',
#         'resnet152',
#         'densenet121',
#         'densenet161',
#         'densenet169',
#         'densenet201',
#         'squeezenet1_1',
#         'shufflenet_v2_x0_5'
#     ]
#     explain_methods = ['Vanilla Backpropagation', 'Deconvolution', 'Guided Backpropagation', 'Grad-CAM', 'Grad-CAM++']
#     dataset_path = os.path.join(os.path.dirname(
#         os.path.dirname(os.getcwd())), 'dataset')
#     output_path = os.path.join(os.path.dirname(
#         os.path.dirname(os.getcwd())), 'vis_out')

#     name_list = np.load(os.path.join(dataset_path, 'name.npy')).tolist()
#     index_list = np.load(os.path.join(dataset_path, 'index.npy')).tolist()
#     model_name = model_list[idx]
#     correct_idx = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'correct_idx.npy'))

#     if os.path.exists(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'correct_name.npy')):
#         correct_name = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'correct_name.npy')).tolist()
#     else:
#         correct_name = []
#         for idx in correct_idx:
#             correct_name.append(name_list[index_list.index(idx)])
#         np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'correct_name.npy'), correct_name)

#     for label in range(minlabel, maxlabel):
#         random_images = getRandom(dataset_path, label)

#         wrg = 0
#         for name in random_images:
#             if name not in correct_name:
#                 wrg += 1
#         print(f'get {len(random_images)} random imgs, {wrg} incorrect')
        
#         demo1(dataset_path, random_images, model_name, output_path, label, explain_methods)
#         print(f'finish: {model_name}, label: {label}, {len(random_images)}')
# if __name__ == '__main__':
#     main()

# # # run BBMP
# model_list = [
#     'mobilenet_v2',
#     'alexnet',
#     'resnet18',
#     'resnet34',
#     'resnet50',
#     'resnet101',
#     'resnet152',
#     'densenet121',
#     'densenet161',
#     'densenet169',
#     'densenet201',
#     'squeezenet1_1',
#     'shufflenet_v2_x0_5'
# ]
# dataset_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'dataset')
# for input_label in range(500, 1000):
#     # image_name = np.load(os.path.join(dataset_path, 'label_info', f'label_{input_label}_imgname.npy')).tolist()[0]
#     img_name_list = getRandom(dataset_path, input_label)
#     print(f'label {input_label}, {len(img_name_list)}')
#     for image_name in img_name_list:
#         output_path =  os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'vis_out')
#         out_path = os.path.join(output_path, os.path.splitext(image_name)[0])
#         for model_name in model_list:
#             BBMP_process(dataset_path, image_name, model_name, out_path)
#     print('finish')
#             # BBMPmask_to_heatmap(dataset_path, image_name, model_name, out_path)

# # run smoothgradcam
# @click.command()
# @click.option('--idx',
#               type=int,
#               default=0,
#               help='model index in the list, range: 0-12')
# @click.option('--minlabel',
#               type=int,
#               default=0,
#               help='min label, range: 0-999 except [638, 664, 744, 782, 818, 836, 848, 885]')
# @click.option('--maxlabel',
#               type=int,
#               default=100,
#               help='max label, range: 0-999 except [638, 664, 744, 782, 818, 836, 848, 885]')
# def main(idx, minlabel, maxlabel):
#     dataset_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'dataset')

#     model_list = [
#         'mobilenet_v2',
#         'alexnet',
#         'resnet18',
#         'resnet34',
#         'resnet50',
#         'resnet101',
#         'resnet152',
#         'densenet121',
#         'densenet161',
#         'densenet169',
#         'densenet201',
#         'squeezenet1_1',
#         'shufflenet_v2_x0_5'
#     ]
#     model_name = model_list[idx]
#     for input_label in range(minlabel, maxlabel):
#         img_name_list = getRandom(dataset_path, input_label)
#         output_path =  os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'test_vis')
#         for image_name in img_name_list:
#             out_path = os.path.join(output_path, os.path.splitext(image_name)[0])
#             os.makedirs(out_path, exist_ok=True)
#             # model_rest = []
#             # smooth_main(dataset_path, image_name, model_name, out_path, True)
#             try:
#                 smooth_main(dataset_path, image_name, model_name, out_path, True)
#             except (RuntimeError):
#                 with open('wrong.txt', 'a') as ftxt:
#                     ftxt.write(f'{model_name}\t{input_label}\t{image_name}\n')
#             # print(model_rest)
#         print(f'{model_name}, finish {input_label}')

# if __name__ == '__main__':
#     main()

# @click.command()
# @click.option('--idx',
#               type=int,
#               default=0,
#               help='model index in the list, range: 0-12')
# @click.option('--inputlabel',
#               type=int,
#               default=0,
#               help='min label, range: 0-999 except [638, 664, 744, 782, 818, 836, 848, 885]')
# def main(idx, inputlabel):
#     dataset_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'dataset')

#     model_list = [
#         'mobilenet_v2',
#         'alexnet',
#         'resnet18',
#         'resnet34',
#         'resnet50',
#         # 'resnet101',
#         # 'resnet152',
#         # 'densenet121',
#         # 'densenet161',
#         # 'densenet169',
#         # 'densenet201',
#         'squeezenet1_1',
#         'shufflenet_v2_x0_5'
#     ]
#     model_name = model_list[idx]
#     img_name_list = getRandom(dataset_path, inputlabel)
#     output_path =  os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'vis_out')
#     for image_name in img_name_list:
#         out_path = os.path.join(output_path, os.path.splitext(image_name)[0])
#         # os.makedirs(out_path, exist_ok=True)
#         # model_rest = []
#         # smooth_main(dataset_path, image_name, model_name, out_path, True)
#         try:
#             smooth_main(dataset_path, image_name, model_name, out_path, True)
#         except (RuntimeError):
#             with open('wrong.txt', 'a') as ftxt:
#                 ftxt.write(f'{model_name}\t{inputlabel}\t{image_name}\n')
#         # print(model_rest)
#     with open('info.txt', 'a') as ftxt:
#         ftxt.write(f'{model_name}\tfinish{inputlabel}\n')

# if __name__ == '__main__':
#     main()