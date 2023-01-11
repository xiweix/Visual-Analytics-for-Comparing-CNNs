import os
import csv
import numpy as np
import json
from utils import idxToID, findParentLabel, IDToWord, IDtoIdx

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
TenColor_list = [
    '#00264d',
    '#003366',
    '#004080',
    '#004d99',
    '#0059b3',
    '#0066cc',
    '#0073e6',
    '#1a8cff',
    '#4da6ff',
    '#80bfff'
]
[a0, a1, a2, a3, a4, a5, a6, a7, a8, a9] = [6.0, 18.0, 30.0, 42.0, 54.0, 60.6, 70.0, 75.6, 78.0, 88.0]
write_path = 'total571NodeInfo.txt'
with open(write_path, 'a') as ftxt:
    ftxt.write('export default {\n')
    ftxt.write('  modelTotalNode: [\n')
total_id = np.load(os.path.join(dataset_path, 'total1579_ID.npy')).tolist()
for model_name in full_model_list:
    print(model_name)
    with open(write_path, 'a') as ftxt:
        ftxt.write('    {\n')
        ftxt.write(f'      model: \'{model_name}\',\n')
        ftxt.write('      modelNodes: [\n')
    total_acc = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'total_11579_accuracy.npy')).tolist()
    for i in range(len(total_acc)):
        if i >= 1000:
            # wordID
            curWordID = total_id[i]
            # name
            if curWordID == 'MISC':
                curLabelName = 'MISC'
            else:
                curLabelName = IDToWord(dataset_path, curWordID)
            # accuracy
            curAcc = float(total_acc[i])
            # _color
            if curAcc >= a0 and curAcc < a1:
                curColor = TenColor_list[0]
            elif curAcc >= a1 and curAcc < a2:
                curColor = TenColor_list[1]
            elif curAcc >= a2 and curAcc < a3:
                curColor = TenColor_list[2]   
            elif curAcc >= a3 and curAcc < a4:
                curColor = TenColor_list[3]  
            elif curAcc >= a4 and curAcc < a5:
                curColor = TenColor_list[4]   
            elif curAcc >= a5 and curAcc < a6:
                curColor = TenColor_list[5]   
            elif curAcc >= a6 and curAcc < a7:
                curColor = TenColor_list[6]   
            elif curAcc >= a7 and curAcc < a8:
                curColor = TenColor_list[7]   
            elif curAcc >= a8 and curAcc < a9:
                curColor = TenColor_list[8]   
            elif curAcc >= a9:
                curColor = TenColor_list[9]
            else:
                print('wrong!')
            # _size
            if i < 1571:
                curSize = 6
            else:
                curSize = 12
            info = '        { id: ' + str(i-1000) + ', name: \'' + curLabelName + '\', _color: \'' + curColor + '\', _size: ' + str(curSize) + ', accuracy: ' + str(curAcc) + ' },\n'
            with open(write_path, 'a') as ftxt:
                ftxt.write(info)
    info = '        { id: ' + str(len(total_acc)-1000) + ', name: \'' + 'ImageNet' + '\', _color: \'' + 'rgba(73,133,183,0.45)' + '\', _size: ' + str(6) + ' }\n'
    with open(write_path, 'a') as ftxt:
        ftxt.write(info)
        ftxt.write('      ],\n')
        ftxt.write('      modelLinks: [\n')
    linkcolor = 'rgba(159,163,167,1)'
    for i in range(len(total_id)):
        if i >= 1000:
            start = i-1000
            if i < 1571:
                curID = total_id[i]
                parIDs = findParentLabel(dataset_path, curID)
                for parID in parIDs:
                    end = IDtoIdx(dataset_path, parID) - 1000
                    linkInfo = '        { sid: ' + str(start) + ', tid: ' + str(end) + ', _color: \'' + linkcolor + '\' },\n'
                    with open(write_path, 'a') as ftxt:
                        ftxt.write(linkInfo)
            elif i >= 1571 and i < 1578:
                end = len(total_id) - 1000
                linkInfo = '        { sid: ' + str(start) + ', tid: ' + str(end) + ', _color: \'' + linkcolor + '\' },\n'
                with open(write_path, 'a') as ftxt:
                    ftxt.write(linkInfo)
            else:
                end = len(total_id) - 1000
                linkInfo = '        { sid: ' + str(start) + ', tid: ' + str(end) + ', _color: \'' + linkcolor + '\' }\n'
                with open(write_path, 'a') as ftxt:
                    ftxt.write(linkInfo)
    if model_name == 'shufflenet_v2_x0_5':
        with open(write_path, 'a') as ftxt:
            ftxt.write('      ]\n')
            ftxt.write('    }\n')
    else:
        with open(write_path, 'a') as ftxt:
            ftxt.write('      ]\n')
            ftxt.write('    },\n')
with open(write_path, 'a') as ftxt:
    ftxt.write('  ]\n')
    ftxt.write('}\n')
# total_parent = np.load(os.path.join(dataset_path, 'parent_name.npy')).tolist()
# total_grand = np.load(os.path.join(dataset_path, 'grandParent_name.npy')).tolist()
# total_label = []
# for label in range(1000):
#     i_ID = idxToID(dataset_path, label)
#     total_label.append(i_ID)
# print(len(total_label), len(total_parent), len(total_grand))
# print(total_label[0], total_parent[0], total_grand[0])
# np.save(os.path.join(dataset_path, 'label1000_name.npy'), total_label)
# total_1579 = []
# total_1579.extend(total_label)
# total_1579.extend(total_parent)
# total_1579.extend(total_grand)
# print(len(total_1579))
# np.save(os.path.join(dataset_path, 'total1579_ID.npy'), total_1579)

# total_parent = np.load(os.path.join(dataset_path, 'parent_name.npy')).tolist()
# total_grand = np.load(os.path.join(dataset_path, 'grandParent_name.npy')).tolist()
# for model_name in full_model_list:
    # accuracy = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'accuracy.npy')).tolist()
    # del accuracy[1000]
    # parent_acc_total = [0 for ii in range(len(total_parent))]
    # parent_acc_count = [0 for ii in range(len(total_parent))]
    # parent_acc = [0 for ii in range(len(total_parent))]
    # for i in range(1000):
    #     i_ID = idxToID(dataset_path, i)
    #     i_Acc = float(accuracy[i])
    #     i_parents = findParentLabel(dataset_path, i_ID)
    #     for i_parent in i_parents:
    #         idx = total_parent.index(i_parent)
    #         parent_acc_total[idx] += i_Acc
    #         parent_acc_count[idx] += 1
    # for j in range(len(parent_acc_total)):
    #     parent_acc[j] = parent_acc_total[j] / parent_acc_count[j]
    #     parent_acc[j] = float("%.3f" % float(parent_acc[j]))
    # np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'parent571_accuracy.npy'), parent_acc)
    # print(model_name, len(parent_acc), parent_acc[107])

    # parent_acc = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'parent571_accuracy.npy')).tolist()
    # grand_acc_total = [0 for ii in range(len(total_grand))]
    # grand_acc_count = [0 for ii in range(len(total_grand))]
    # grand_acc = [0 for ii in range(len(total_grand))]
    # for i in range(len(total_parent)):
    #     i_ID = total_parent[i]
    #     i_Acc = float(parent_acc[i])
    #     i_parents = findParentLabel(dataset_path, i_ID)
    #     for i_parent in i_parents:
    #         idx = total_grand.index(i_parent)
    #         grand_acc_total[idx] += i_Acc
    #         grand_acc_count[idx] += 1
    # print(np.max(grand_acc_count), grand_acc_count.index(np.max(grand_acc_count)))
    # for j in range(len(grand_acc_total)):
    #     grand_acc[j] = grand_acc_total[j] / grand_acc_count[j]
    #     grand_acc[j] = float("%.3f" % float(grand_acc[j]))
    # np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'grand8_accuracy.npy'), grand_acc)
    # print(model_name, len(grand_acc), grand_acc_total[grand_acc_count.index(np.max(grand_acc_count))], grand_acc[grand_acc_count.index(np.max(grand_acc_count))])

    # accuracy = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'accuracy.npy')).tolist()
    # del accuracy[1000]
    # label_acc = []
    # for acc in accuracy:
    #     label_acc.append(float("%.3f" % float(acc)))
    # print(len(label_acc))
    # np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'label1000_accuracy.npy'), label_acc)

    # total_acc = []
    # label_acc = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'label1000_accuracy.npy')).tolist()
    # parent_acc = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'parent571_accuracy.npy')).tolist()
    # grand_acc = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'grand8_accuracy.npy')).tolist()
    # total_acc.extend(label_acc)
    # total_acc.extend(parent_acc)
    # total_acc.extend(grand_acc)

    # print(len(total_acc))
    # np.save(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'total_11579_accuracy.npy'), total_acc)


# dataset_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'dataset')
# # word = []
# # with open(os.path.join(dataset_path, 'id_word.json'), 'r') as f:
# #     pattern_IDToWord = json.loads(f.read())
# #     for pattern in pattern_IDToWord:
# #         if pattern_IDToWord[pattern] not in word:
# #             word.append(pattern_IDToWord[pattern])
# #         else:
# #             print(pattern)
# #             print(pattern_IDToWord[pattern])

# # # no data in n00523513
# tree_roots = ['n00007846', 'n00015388', 'n00017222', 'n00019128', 'n00021939', 'n00523513', 'n09287968', 'n12992868', 'MISC']
# root0 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[0]}.npy')).tolist()
# root1 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[1]}.npy')).tolist()
# root2 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[2]}.npy')).tolist()
# root3 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[3]}.npy')).tolist()
# root4 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[4]}.npy')).tolist()
# root5 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[5]}.npy')).tolist()
# root6 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[6]}.npy')).tolist()
# root7 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[7]}.npy')).tolist()
# combo = root0 + root1 + root2 + root3 + root4 + root5 + root6 + root7
# # total_parent = []
# # total_parent_content = []
# # for label in range(1000):
# #     ID = idxToID(dataset_path, label)
# #     parentID = findParentLabel(dataset_path, ID)
# #     for parent in parentID:
# #         parentContent = IDToWord(dataset_path, parent)
# #         # if parentContent == 'cap':
# #         #     print(parent, parentContent)
# #         #     if parent in combo:
# #         #         if parent in root0:
# #         #             print(parent, '0')
# #         #         if parent in root1:
# #         #             print(parent, '1')
# #         #         if parent in root2:
# #         #             print(parent, '2')
# #         #         if parent in root3:
# #         #             print(parent, '3')
# #         #         if parent in root4:
# #         #             print(parent, '4')
# #         #         if parent in root5:
# #         #             print(parent, '5')
# #         #         if parent in root6:
# #         #             print(parent, '6')
# #         #         if parent in root7:
# #         #             print(parent, '7')
# #         #     else:
# #         #         print(parent, '8')
# #         # if parentContent == 'table':
# #         #     print(parent, parentContent)
# #         #     if parent in combo:
# #         #         if parent in root0:
# #         #             print(parent, '0')
# #         #         if parent in root1:
# #         #             print(parent, '1')
# #         #         if parent in root2:
# #         #             print(parent, '2')
# #         #         if parent in root3:
# #         #             print(parent, '3')
# #         #         if parent in root4:
# #         #             print(parent, '4')
# #         #         if parent in root5:
# #         #             print(parent, '5')
# #         #         if parent in root6:
# #         #             print(parent, '6')
# #         #         if parent in root7:
# #         #             print(parent, '7')
# #         #     else:
# #         #         print(parent, '8')
# #         # if parentContent == 'helmet':
# #             # print(parent, parentContent)
# #             # if parent in combo:
# #             #     if parent in root0:
# #             #         print(parent, '0')
# #             #     if parent in root1:
# #             #         print(parent, '1')
# #             #     if parent in root2:
# #             #         print(parent, '2')
# #             #     if parent in root3:
# #             #         print(parent, '3')
# #             #     if parent in root4:
# #             #         print(parent, '4')
# #             #     if parent in root5:
# #             #         print(parent, '5')
# #             #     if parent in root6:
# #             #         print(parent, '6')
# #             #     if parent in root7:
# #             #         print(parent, '7')
# #             # else:
# #             #     print(parent, '8')
# #         # if parentContent == 'support':
# #         #     print(parent, parentContent)
# #         #     if parent in combo:
# #         #         if parent in root0:
# #         #             print(parent, '0')
# #         #         if parent in root1:
# #         #             print(parent, '1')
# #         #         if parent in root2:
# #         #             print(parent, '2')
# #         #         if parent in root3:
# #         #             print(parent, '3')
# #         #         if parent in root4:
# #         #             print(parent, '4')
# #         #         if parent in root5:
# #         #             print(parent, '5')
# #         #         if parent in root6:
# #         #             print(parent, '6')
# #         #         if parent in root7:
# #         #             print(parent, '7')
# #         #     else:
# #         #         print(parent, '8')
# #         # if parentContent == 'lamp':
# #         #     print(parent, parentContent)
# #         #     if parent in combo:
# #         #         if parent in root0:
# #         #             print(parent, '0')
# #         #         if parent in root1:
# #         #             print(parent, '1')
# #         #         if parent in root2:
# #         #             print(parent, '2')
# #         #         if parent in root3:
# #         #             print(parent, '3')
# #         #         if parent in root4:
# #         #             print(parent, '4')
# #         #         if parent in root5:
# #         #             print(parent, '5')
# #         #         if parent in root6:
# #         #             print(parent, '6')
# #         #         if parent in root7:
# #         #             print(parent, '7')
# #         #     else:
# #         #         print(parent, '8')
# #         if parentContent == 'dish':
# #             print(parent, parentContent)
# #             if parent in combo:
# #                 if parent in root0:
# #                     print(parent, '0')
# #                 if parent in root1:
# #                     print(parent, '1')
# #                 if parent in root2:
# #                     print(parent, '2')
# #                 if parent in root3:
# #                     print(parent, '3')
# #                 if parent in root4:
# #                     print(parent, '4')
# #                 if parent in root5:
# #                     print(parent, '5')
# #                 if parent in root6:
# #                     print(parent, '6')
# #                 if parent in root7:
# #                     print(parent, '7')
# #             else:
# #                 print(parent, '8')
# total_500 = []
# total_8 = []
# # write_path = os.path.join(dataset_path, 'IDtoParentIDTotal.txt')
# # write_path2 = os.path.join(dataset_path, 'idxtoIDTotal.txt')
# # write_path3 = os.path.join(dataset_path, 'IDtoIdxTotal.txt')

# # with open(write_path, 'a') as ftxt:
# #     ftxt.write('{\n')
# # with open(write_path2, 'a') as ftxt:
# #     ftxt.write('{\n')
# # with open(write_path3, 'a') as ftxt:
# #     ftxt.write('{\n')
# for label in range(1000):
#     ID = idxToID(dataset_path, label)
#     # with open(write_path2, 'a') as ftxt:
#     #     ftxt.write(f'\"{label}\": \"{ID}\",\n')
#     # with open(write_path3, 'a') as ftxt:
#     #     ftxt.write(f'\"{ID}\": \"{label}\",\n')
#     parentIDs = findParentLabel(dataset_path, ID)
#     ID_Parents = []
#     for parentID in parentIDs:
#         if parentID in ['n02954340', 'n02954938', 'n02955065']:
#             parentID = 'n02954340'
#         elif parentID in ['n04379243', 'n04379964']:
#             parentID = 'n04379243'
#         elif parentID in ['n03513137', 'n03513376']:
#             parentID = 'n03513137'
#         elif parentID in ['n04360501', 'n04359589']:
#             parentID = 'n04360501'
#         elif parentID in ['n03636248', 'n03636649']:
#             parentID = 'n03636248'
#         elif parentID in ['n03206908', 'n07557434']:
#             parentID = 'n03206908'
#         if parentID not in ID_Parents:
#             ID_Parents.append(parentID)
#         if parentID not in total_500:
#             total_500.append(parentID)
#     # with open(write_path, 'a') as ftxt:
#     #     ftxt.write(f'\"{ID}\": {ID_Parents},\n')
# print(len(total_500))
# np.save(os.path.join(dataset_path, 'parent_name.npy'), total_500)
# for i in range(len(total_500)):
#     idx = i + 1000
#     parent = total_500[i]
#     # with open(write_path2, 'a') as ftxt:
#     #     ftxt.write(f'\"{idx}\": \"{parent}\",\n')
#     # with open(write_path3, 'a') as ftxt:
#     #     ftxt.write(f'\"{parent}\": \"{idx}\",\n')
#     grandIDs = []
#     if parent in combo:
#         if parent in root0:
#             grandIDs.append(tree_roots[0])
#         if parent in root1:
#             grandIDs.append(tree_roots[1])
#         if parent in root2:
#             grandIDs.append(tree_roots[2])
#         if parent in root3:
#             grandIDs.append(tree_roots[3])
#         if parent in root4:
#             grandIDs.append(tree_roots[4])
#         if parent in root5:
#             grandIDs.append(tree_roots[5])
#         if parent in root6:
#             grandIDs.append(tree_roots[6])
#         if parent in root7:
#             grandIDs.append(tree_roots[7])
#     else:
#         grandIDs.append(tree_roots[8])
#     if len(grandIDs) != 1:
#         print(parent, grandIDs)
#     for grand in grandIDs:
#         if grand not in total_8:
#             total_8.append(grand)
#     # with open(write_path, 'a') as ftxt:
#     #     ftxt.write(f'\"{parent}\": {grandIDs},\n')
# print(len(total_8))
# print(total_8)
# np.save(os.path.join(dataset_path, 'grandParent_name.npy'), total_8)
# for i in range(len(total_8)):
#     idx = i + 1000 + len(total_500)
#     grandParent = total_8[i]
#     # with open(write_path2, 'a') as ftxt:
#     #     ftxt.write(f'\"{idx}\": \"{grandParent}\",\n')
#     # with open(write_path3, 'a') as ftxt:
#     #     ftxt.write(f'\"{grandParent}\": \"{idx}\",\n')
# # with open(write_path, 'a') as ftxt:
# #     ftxt.write('}\n')
# # with open(write_path2, 'a') as ftxt:
# #     ftxt.write('}\n')
# # with open(write_path3, 'a') as ftxt:
# #     ftxt.write('}\n')