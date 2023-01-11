import os
import csv
import numpy as np

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
Orgcolor_list = [
    '#00264d',
    '#003366',
    '#004080',
    '#004d99',
    '#0059b3',
    '#0066cc',
    '#0073e6',
    '#0080ff',
    '#1a8cff',
    '#3399ff',
    '#4da6ff',
    '#66b3ff',
    '#80bfff'
]
Orgsize_list = [
    6,
    9,
    12,
    15,
    18,
    21,
    24,
    27,
    30,
    33,
    36,
    39,
    42
]
sizes_name = [6]
sort_param_idx_list = np.argsort(full_model_param)
size_list = [0 for i in range(len(full_model_list))]
i = 0
for idx in sort_param_idx_list:
    size_list[idx] = Orgsize_list[i]
    i += 1
sizes_name.extend(size_list)
# print(sizes_name)
params_name = [6666]
params_name.extend(full_model_param)

write_path = 'modelNodeData.txt'
with open(write_path, 'a') as ftxt:
    ftxt.write('export default {\n')
    ftxt.write('  labelNodeInfo: [\n')

csv_path = os.path.join(dataset_path, 'ImageNet_Val', 'accuracy_analysis1.csv')
with open(csv_path, 'r') as fcsv:
    prj_info = csv.reader(fcsv)
    for line in prj_info:
        if prj_info.line_num == 1:
            name_list = line
        elif prj_info.line_num < 1001:
            curLabel = prj_info.line_num - 2
            with open(write_path, 'a') as ftxt:
                ftxt.write('    {\n')
                ftxt.write(f'      id: {curLabel},\n')
                ftxt.write('      content: [\n')
            models_name = ['imageNet']
            colors_name = ['rgba(73,133,183,0.45)']
            accuracies_name = [6666]
            models_name.extend(full_model_list)
            labelAccuracy = []
            for ii in range(len(line)):
                labelAccuracy.append("%.1f" % float(line[ii]))
            sort_labelAccuracy_idx_list = np.argsort(labelAccuracy)
            color_list = [0 for i in range(len(full_model_list))]
            i = 0
            for idx in sort_labelAccuracy_idx_list:
                color_list[idx] = Orgcolor_list[i]
                i += 1
            colors_name.extend(color_list)
            accuracies_name.extend(labelAccuracy)

            for j in range(len(models_name)):
                if j == len(models_name) - 1:
                    info = '        { id: ' + str(j) + ', name: \'' + models_name[j] +'\', _color: \'' + colors_name[j] + '\', _size: ' + str(sizes_name[j]) + ', accuracy: ' + str(accuracies_name[j]) + ', param: ' + str(params_name[j]) + ' }\n'
                else:
                    info = '        { id: ' + str(j) + ', name: \'' + models_name[j] +'\', _color: \'' + colors_name[j] + '\', _size: ' + str(sizes_name[j]) + ', accuracy: ' + str(accuracies_name[j]) + ', param: ' + str(params_name[j]) + ' },\n'
                with open(write_path, 'a') as ftxt:
                    ftxt.write(info)
            with open(write_path, 'a') as ftxt:
                ftxt.write('      ]\n')
                ftxt.write('    },\n')
        elif prj_info.line_num == 1001:
            curLabel = prj_info.line_num - 2
            with open(write_path, 'a') as ftxt:
                ftxt.write('    {\n')
                ftxt.write(f'      id: {curLabel},\n')
                ftxt.write('      content: [\n')
            models_name = ['imageNet']
            colors_name = ['rgba(73,133,183,0.45)']
            accuracies_name = [6666]
            models_name.extend(full_model_list)
            labelAccuracy = []
            for ii in range(len(line)):
                labelAccuracy.append("%.1f" % float(line[ii]))
            sort_labelAccuracy_idx_list = np.argsort(labelAccuracy)
            color_list = [0 for i in range(len(full_model_list))]
            i = 0
            for idx in sort_labelAccuracy_idx_list:
                color_list[idx] = Orgcolor_list[i]
                i += 1
            colors_name.extend(color_list)
            accuracies_name.extend(labelAccuracy)

            for j in range(len(models_name)):
                if j == len(models_name) - 1:
                    info = '        { id: ' + str(j) + ', name: \'' + models_name[j] +'\', _color: \'' + colors_name[j] + '\', _size: ' + str(sizes_name[j]) + ', accuracy: ' + str(accuracies_name[j]) + ', param: ' + str(params_name[j]) + ' }\n'
                else:
                    info = '        { id: ' + str(j) + ', name: \'' + models_name[j] +'\', _color: \'' + colors_name[j] + '\', _size: ' + str(sizes_name[j]) + ', accuracy: ' + str(accuracies_name[j]) + ', param: ' + str(params_name[j]) + ' },\n'
                with open(write_path, 'a') as ftxt:
                    ftxt.write(info)
            with open(write_path, 'a') as ftxt:
                ftxt.write('      ]\n')
                ftxt.write('    }\n')
                ftxt.write('  ],\n')
        elif prj_info.line_num == 1002:
            with open(write_path, 'a') as ftxt:
                ftxt.write('  modelNodeInfo: [\n')
            models_name = ['imageNet']
            colors_name = ['rgba(73,133,183,0.45)']
            accuracies_name = [6666]
            models_name.extend(full_model_list)
            labelAccuracy = []
            for ii in range(len(line)):
                labelAccuracy.append("%.3f" % float(line[ii]))
            sort_labelAccuracy_idx_list = np.argsort(labelAccuracy)
            color_list = [0 for i in range(len(full_model_list))]
            i = 0
            for idx in sort_labelAccuracy_idx_list:
                color_list[idx] = Orgcolor_list[i]
                i += 1
            colors_name.extend(color_list)
            accuracies_name.extend(labelAccuracy)

            for j in range(len(models_name)):
                if j == len(models_name) - 1:
                    info = '    { id: ' + str(j) + ', name: \'' + models_name[j] +'\', _color: \'' + colors_name[j] + '\', _size: ' + str(sizes_name[j]) + ', accuracy: ' + str(accuracies_name[j]) + ', param: ' + str(params_name[j]) + ' }\n'
                else:
                    info = '    { id: ' + str(j) + ', name: \'' + models_name[j] +'\', _color: \'' + colors_name[j] + '\', _size: ' + str(sizes_name[j]) + ', accuracy: ' + str(accuracies_name[j]) + ', param: ' + str(params_name[j]) + ' },\n'
                with open(write_path, 'a') as ftxt:
                    ftxt.write(info)
            with open(write_path, 'a') as ftxt:
                ftxt.write('  ]\n')
                ftxt.write('}\n')
        else:
            print('wrong!')
     
