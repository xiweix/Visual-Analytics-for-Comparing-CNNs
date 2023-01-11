import os
import numpy as np
from utils import idxToWord

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
grand_info = np.load(os.path.join(dataset_path, 'total1000_grandID.npy')).tolist()

write_path = 'scatterModel.txt'
with open(write_path, 'a') as ftxt:
    ftxt.write('export default {\n')
    ftxt.write('  scatterInfo: [\n')
for model_name in full_model_list:
    coords = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'scatterCoords.npy'))
    accuracy = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'accuracy.npy')).tolist()
    X_idx = coords[:, 0]
    Y_idx = coords[:, 1]
    save_info = [[] for x in range(8)]
    for i in range(X_idx.shape[0]):
        x_coor = X_idx[i]
        y_coor = Y_idx[i]
        curLabel = idxToWord(dataset_path, i)
        cur_group = grand_name[tree_roots.index(grand_info[i])]
        save_list = []
        save_list.append(x_coor)
        save_list.append(y_coor)
        save_list.append(curLabel)
        save_list.append(cur_group)
        save_list.append(i)
        save_list.append(tree_roots.index(grand_info[i]))
        save_list.append("%.1f" % float(accuracy[i]))
        save_info[tree_roots.index(grand_info[i])].append(save_list)
    with open(write_path, 'a') as ftxt:
        ftxt.write('    {\n')
        ftxt.write(f'      model: \'{model_name}\',\n')
        ftxt.write('      content: [\n')
    for j in range(len(save_info)):
        if j == len(save_info) - 1:
          with open(write_path, 'a') as ftxt:
              ftxt.write(f'        {save_info[j]}\n')  
        else:
          with open(write_path, 'a') as ftxt:
              ftxt.write(f'        {save_info[j]},\n')  
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
