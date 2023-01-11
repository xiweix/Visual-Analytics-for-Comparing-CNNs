import os
import numpy as np
from utils import IDToWord, idxToID

write_path = 'barData.txt'
with open(write_path, 'a') as ftxt:
    ftxt.write('export default {\n')
    ftxt.write('  barLabelInfo: [\n')
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
tree_roots = ['n00015388', 'n00021939', 'MISC', 'n00019128', 'n09287968', 'n00007846', 'n00017222', 'n12992868']
grand_name = ['animal', 'artifact', 'MISC', 'natural object', 'geological formation', 'person', 'plant', 'fungus']
root0 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[0]}.npy')).tolist()
root1 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[1]}.npy')).tolist()
root2 = []
root3 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[3]}.npy')).tolist()
root4 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[4]}.npy')).tolist()
root5 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[5]}.npy')).tolist()
root6 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[6]}.npy')).tolist()
root7 = np.load(os.path.join(dataset_path, 'tree_info', f'{tree_roots[7]}.npy')).tolist()
combo = root0 + root1 + root3 + root4 + root5 + root6 + root7
# root_name = []
# for name in tree_roots:
#     if name != 'MISC':
#         root_name.append(IDToWord(dataset_path, name))
#     else: root_name.append('MISC')
# print(root_name)
# print(grand_name)

acc_0 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[0]}', 'accuracy.npy')).tolist()
del acc_0[1000]
acc_1 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[1]}', 'accuracy.npy')).tolist()
del acc_1[1000]
acc_2 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[2]}', 'accuracy.npy')).tolist()
del acc_2[1000]
acc_3 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[3]}', 'accuracy.npy')).tolist()
del acc_3[1000]
acc_4 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[4]}', 'accuracy.npy')).tolist()
del acc_4[1000]
acc_5 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[5]}', 'accuracy.npy')).tolist()
del acc_5[1000]
acc_6 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[6]}', 'accuracy.npy')).tolist()
del acc_6[1000]
acc_7 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[7]}', 'accuracy.npy')).tolist()
del acc_7[1000]
acc_8 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[8]}', 'accuracy.npy')).tolist()
del acc_8[1000]
acc_9 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[9]}', 'accuracy.npy')).tolist()
del acc_9[1000]
acc_10 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[10]}', 'accuracy.npy')).tolist()
del acc_10[1000]
acc_11 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[11]}', 'accuracy.npy')).tolist()
del acc_11[1000]
acc_12 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{full_model_list[12]}', 'accuracy.npy')).tolist()
del acc_12[1000]

AccList = [[[] for x in range(13)] for y in range(8)]
LabelList = [[] for z in range(8)]

for label in range(1000):
    # print(label)
    labelID = idxToID(dataset_path, label)
    if labelID in combo:
        if labelID in root0:
            AccList[0][0].append(acc_0[label])
            AccList[0][1].append(acc_1[label])
            AccList[0][2].append(acc_2[label])
            AccList[0][3].append(acc_3[label])
            AccList[0][4].append(acc_4[label])
            AccList[0][5].append(acc_5[label])
            AccList[0][6].append(acc_6[label])
            AccList[0][7].append(acc_7[label])
            AccList[0][8].append(acc_8[label])
            AccList[0][9].append(acc_9[label])
            AccList[0][10].append(acc_10[label])
            AccList[0][11].append(acc_11[label])
            AccList[0][12].append(acc_12[label])
            LabelList[0].append(label)
            # print(labelID, '0:', len(AccList[0][9]), len(LabelList[0]))
        if labelID in root1:
            AccList[1][0].append(acc_0[label])
            AccList[1][1].append(acc_1[label])
            AccList[1][2].append(acc_2[label])
            AccList[1][3].append(acc_3[label])
            AccList[1][4].append(acc_4[label])
            AccList[1][5].append(acc_5[label])
            AccList[1][6].append(acc_6[label])
            AccList[1][7].append(acc_7[label])
            AccList[1][8].append(acc_8[label])
            AccList[1][9].append(acc_9[label])
            AccList[1][10].append(acc_10[label])
            AccList[1][11].append(acc_11[label])
            AccList[1][12].append(acc_12[label])
            LabelList[1].append(label)
            # print(labelID, '1:', len(AccList[1][7]), len(LabelList[1]))
        if labelID in root3:
            AccList[3][0].append(acc_0[label])
            AccList[3][1].append(acc_1[label])
            AccList[3][2].append(acc_2[label])
            AccList[3][3].append(acc_3[label])
            AccList[3][4].append(acc_4[label])
            AccList[3][5].append(acc_5[label])
            AccList[3][6].append(acc_6[label])
            AccList[3][7].append(acc_7[label])
            AccList[3][8].append(acc_8[label])
            AccList[3][9].append(acc_9[label])
            AccList[3][10].append(acc_10[label])
            AccList[3][11].append(acc_11[label])
            AccList[3][12].append(acc_12[label])
            LabelList[3].append(label)
            # print(labelID, '3:', len(AccList[3][3]), len(LabelList[3]))
        if labelID in root4:
            AccList[4][0].append(acc_0[label])
            AccList[4][1].append(acc_1[label])
            AccList[4][2].append(acc_2[label])
            AccList[4][3].append(acc_3[label])
            AccList[4][4].append(acc_4[label])
            AccList[4][5].append(acc_5[label])
            AccList[4][6].append(acc_6[label])
            AccList[4][7].append(acc_7[label])
            AccList[4][8].append(acc_8[label])
            AccList[4][9].append(acc_9[label])
            AccList[4][10].append(acc_10[label])
            AccList[4][11].append(acc_11[label])
            AccList[4][12].append(acc_12[label])
            LabelList[4].append(label)
            # print(labelID, '4:', len(AccList[4][6]), len(LabelList[4]))
        if labelID in root5:
            AccList[5][0].append(acc_0[label])
            AccList[5][1].append(acc_1[label])
            AccList[5][2].append(acc_2[label])
            AccList[5][3].append(acc_3[label])
            AccList[5][4].append(acc_4[label])
            AccList[5][5].append(acc_5[label])
            AccList[5][6].append(acc_6[label])
            AccList[5][7].append(acc_7[label])
            AccList[5][8].append(acc_8[label])
            AccList[5][9].append(acc_9[label])
            AccList[5][10].append(acc_10[label])
            AccList[5][11].append(acc_11[label])
            AccList[5][12].append(acc_12[label])
            LabelList[5].append(label)
            # print(labelID, '5:', len(AccList[5][7]), len(LabelList[5]))
        if labelID in root6:
            AccList[6][0].append(acc_0[label])
            AccList[6][1].append(acc_1[label])
            AccList[6][2].append(acc_2[label])
            AccList[6][3].append(acc_3[label])
            AccList[6][4].append(acc_4[label])
            AccList[6][5].append(acc_5[label])
            AccList[6][6].append(acc_6[label])
            AccList[6][7].append(acc_7[label])
            AccList[6][8].append(acc_8[label])
            AccList[6][9].append(acc_9[label])
            AccList[6][10].append(acc_10[label])
            AccList[6][11].append(acc_11[label])
            AccList[6][12].append(acc_12[label])
            LabelList[6].append(label)
            # print(labelID, '6:', len(AccList[6][8]), len(LabelList[6]))
        if labelID in root7:
            AccList[7][0].append(acc_0[label])
            AccList[7][1].append(acc_1[label])
            AccList[7][2].append(acc_2[label])
            AccList[7][3].append(acc_3[label])
            AccList[7][4].append(acc_4[label])
            AccList[7][5].append(acc_5[label])
            AccList[7][6].append(acc_6[label])
            AccList[7][7].append(acc_7[label])
            AccList[7][8].append(acc_8[label])
            AccList[7][9].append(acc_9[label])
            AccList[7][10].append(acc_10[label])
            AccList[7][11].append(acc_11[label])
            AccList[7][12].append(acc_12[label])
            LabelList[7].append(label)
            # print(labelID, '7:', len(AccList[7][9]), len(LabelList[7]))
    else:
        AccList[2][0].append(acc_0[label])
        AccList[2][1].append(acc_1[label])
        AccList[2][2].append(acc_2[label])
        AccList[2][3].append(acc_3[label])
        AccList[2][4].append(acc_4[label])
        AccList[2][5].append(acc_5[label])
        AccList[2][6].append(acc_6[label])
        AccList[2][7].append(acc_7[label])
        AccList[2][8].append(acc_8[label])
        AccList[2][9].append(acc_9[label])
        AccList[2][10].append(acc_10[label])
        AccList[2][11].append(acc_11[label])
        AccList[2][12].append(acc_12[label])
        LabelList[2].append(label)
        # print(labelID, '2:', len(AccList[2][2]), len(LabelList[2]))
# for kkkkk in range(8):
#     print(kkkkk, len(AccList[kkkkk][12]), len(LabelList[kkkkk]))
for i in range(len(AccList)):
    parent_label = grand_name[i]
    TotalAccInfo = AccList[i]
    # print('TotalAccInfo', len(TotalAccInfo))
    label_name = LabelList[i]
    info = '      label: \'' + parent_label + '\',\n'
    with open(write_path, 'a') as ftxt:
        ftxt.write('    {\n')
        ftxt.write(info)
        ftxt.write('      modelsInfo: [\n')

    for j in range(len(TotalAccInfo)):
        save_model = full_model_list[j]
        modelAcc = TotalAccInfo[j]
        sortIndex = np.argsort(modelAcc).tolist()
        # print(len(label_name), len(modelAcc), len(sortIndex))
        sortIndex.reverse()
        if len(sortIndex) < 10:
            print(parent_label, save_model)
            save_labelList = []
            save_labelAcc = []
            for k in range(len(sortIndex)):
                save_labelList.append(str(label_name[sortIndex[k]]))
                save_labelAcc.append(float("%.1f" % float(modelAcc[sortIndex[k]])))
        else:
            save_labelList = []
            save_labelAcc = []
            save_labelList.append(str(label_name[sortIndex[0]]))
            save_labelAcc.append(float("%.1f" % float(modelAcc[sortIndex[0]])))
            save_labelList.append(str(label_name[sortIndex[1]]))
            save_labelAcc.append(float("%.1f" % float(modelAcc[sortIndex[1]])))
            save_labelList.append(str(label_name[sortIndex[2]]))
            save_labelAcc.append(float("%.1f" % float(modelAcc[sortIndex[2]])))
            save_labelList.append(str(label_name[sortIndex[3]]))
            save_labelAcc.append(float("%.1f" % float(modelAcc[sortIndex[3]])))
            save_labelList.append(str(label_name[sortIndex[4]]))
            save_labelAcc.append(float("%.1f" % float(modelAcc[sortIndex[4]])))
            sortIndex.reverse()
            save_labelList.append(str(label_name[sortIndex[4]]))
            save_labelAcc.append(float("%.1f" % float(modelAcc[sortIndex[4]])))
            save_labelList.append(str(label_name[sortIndex[3]]))
            save_labelAcc.append(float("%.1f" % float(modelAcc[sortIndex[3]])))
            save_labelList.append(str(label_name[sortIndex[2]]))
            save_labelAcc.append(float("%.1f" % float(modelAcc[sortIndex[2]])))
            save_labelList.append(str(label_name[sortIndex[1]]))
            save_labelAcc.append(float("%.1f" % float(modelAcc[sortIndex[1]])))
            save_labelList.append(str(label_name[sortIndex[0]]))
            save_labelAcc.append(float("%.1f" % float(modelAcc[sortIndex[0]])))
        model_info = '          model: \'' + save_model + '\',\n'
        labelList_info = '          labelList: ' + str(save_labelList) + ',\n'
        labelAcc_info = '          labelAcc: ' + str(save_labelAcc) + '\n'
        if j == len(TotalAccInfo) - 1:
            with open(write_path, 'a') as ftxt:
                ftxt.write('        {\n')
                ftxt.write(model_info)
                ftxt.write(labelList_info)
                ftxt.write(labelAcc_info)
                ftxt.write('        }\n')
        else:
            with open(write_path, 'a') as ftxt:
                ftxt.write('        {\n')
                ftxt.write(model_info)
                ftxt.write(labelList_info)
                ftxt.write(labelAcc_info)
                ftxt.write('        },\n')
    if i == len(AccList) - 1:
        with open(write_path, 'a') as ftxt:
            ftxt.write('      ]\n')
            ftxt.write('    }\n')
    else:
        with open(write_path, 'a') as ftxt:
            ftxt.write('      ]\n')
            ftxt.write('    },\n')
with open(write_path, 'a') as ftxt:
    ftxt.write('  ],\n')
    ftxt.write('  barModelInfo: [\n')

for iii in range(len(full_model_list)):
    save_model = full_model_list[iii]
    acc_0 = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{save_model}', 'accuracy.npy')).tolist()
    del acc_0[1000]
    sortIndex = np.argsort(acc_0).tolist()
    sortIndex.reverse()
    save_labelList = []
    save_labelAcc = []
    save_labelList.append(str(sortIndex[0]))
    save_labelAcc.append(float("%.1f" % float(acc_0[sortIndex[0]])))
    save_labelList.append(str(sortIndex[1]))
    save_labelAcc.append(float("%.1f" % float(acc_0[sortIndex[1]])))
    save_labelList.append(str(sortIndex[2]))
    save_labelAcc.append(float("%.1f" % float(acc_0[sortIndex[2]])))
    save_labelList.append(str(sortIndex[3]))
    save_labelAcc.append(float("%.1f" % float(acc_0[sortIndex[3]])))
    save_labelList.append(str(sortIndex[4]))
    save_labelAcc.append(float("%.1f" % float(acc_0[sortIndex[4]])))
    sortIndex.reverse()
    save_labelList.append(str(sortIndex[4]))
    save_labelAcc.append(float("%.1f" % float(acc_0[sortIndex[4]])))
    save_labelList.append(str(sortIndex[3]))
    save_labelAcc.append(float("%.1f" % float(acc_0[sortIndex[3]])))
    save_labelList.append(str(sortIndex[2]))
    save_labelAcc.append(float("%.1f" % float(acc_0[sortIndex[2]])))
    save_labelList.append(str(sortIndex[1]))
    save_labelAcc.append(float("%.1f" % float(acc_0[sortIndex[1]])))
    save_labelList.append(str(sortIndex[0]))
    save_labelAcc.append(float("%.1f" % float(acc_0[sortIndex[0]])))
    model_info = '      model: \'' + save_model + '\',\n'
    labelList_info = '      labelList: ' + str(save_labelList) + ',\n'
    labelAcc_info = '      labelAcc: ' + str(save_labelAcc) + '\n'
    if iii == len(full_model_list) - 1:
        with open(write_path, 'a') as ftxt:
            ftxt.write('    {\n')
            ftxt.write(model_info)
            ftxt.write(labelList_info)
            ftxt.write(labelAcc_info)
            ftxt.write('    }\n')
    else:
        with open(write_path, 'a') as ftxt:
            ftxt.write('    {\n')
            ftxt.write(model_info)
            ftxt.write(labelList_info)
            ftxt.write(labelAcc_info)
            ftxt.write('    },\n')
with open(write_path, 'a') as ftxt:
    ftxt.write('  ]\n')
    ftxt.write('}\n')