import os
import csv
from utils import idxToWord

dataset_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'dataset')
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
colors = [
    'rgba(27,36,49,1)',
    'rgba(150,45,73,1)',
    'rgba(230,165,127,1)',
    'rgba(248,228,126,1)',
    'rgba(128,196,169,1)',
    'rgba(75,120,155,1)',
    'rgba(89,70,112,1)',
    'rgba(216,118,120,1)',
    'rgba(190,114,73,1)',
    'rgba(149,128,74,1)',
    'rgba(45,83,96,1)',
    'rgba(89,60,80,1)',
    'rgba(237,122,158,1)'
]
write_path = 'scatterData.txt'
with open(write_path, 'a') as ftxt:
    ftxt.write('export default {\n')
    ftxt.write('  labelInfo: [\n')
csv_path = os.path.join(dataset_path, 'ImageNet_Val', 'accuracy_analysis1.csv')
with open(csv_path, 'r') as fcsv:
    prj_info = csv.reader(fcsv)
    for line in prj_info:
        if prj_info.line_num == 1:
            name_list = line
        elif prj_info.line_num < 1001:
            curLabel = prj_info.line_num - 2
            curLabelName = idxToWord(dataset_path, curLabel)
            curLabelName = curLabelName.split(',')[0]
            with open(write_path, 'a') as ftxt:
                ftxt.write('    {\n')
                ftxt.write(f'      label: {curLabel},\n')
                ftxt.write(f'      labelname: \'{curLabelName}\',\n')
                ftxt.write('      content: [\n')
            for ii in range(len(line)):
                model_acc = float("%.1f" % float(line[ii]))
                model_param = full_model_param[ii] / 10000000.
                model_name = name_list[ii]
                if ii == len(line) - 1:
                    info = '        [[' + str(model_param) + ', ' + str(model_acc) + ', ' + '\'' + model_name + '\']]\n'
                else:
                    info = '        [[' + str(model_param) + ', ' + str(model_acc) + ', ' + '\'' + model_name + '\']],\n'
                with open(write_path, 'a') as ftxt:
                    ftxt.write(info)
            with open(write_path, 'a') as ftxt:
                ftxt.write('      ]\n')
                ftxt.write('    },\n')
        elif prj_info.line_num == 1001:
            curLabel = prj_info.line_num - 2
            curLabelName = idxToWord(dataset_path, curLabel)
            curLabelName = curLabelName.split(',')[0]
            with open(write_path, 'a') as ftxt:
                ftxt.write('    {\n')
                ftxt.write(f'      label: {curLabel},\n')
                ftxt.write(f'      labelname: \'{curLabelName}\',\n')
                ftxt.write('      content: [\n')
            for ii in range(len(line)):
                model_acc = float("%.1f" % float(line[ii]))
                model_param = full_model_param[ii] / 10000000.
                model_name = name_list[ii]
                if ii == len(line) - 1:
                    info = '        [[' + str(model_param) + ', ' + str(model_acc) + ', ' + '\'' + model_name + '\']]\n'
                else:
                    info = '        [[' + str(model_param) + ', ' + str(model_acc) + ', ' + '\'' + model_name + '\']],\n'
                with open(write_path, 'a') as ftxt:
                    ftxt.write(info)
            with open(write_path, 'a') as ftxt:
                ftxt.write('      ]\n')
                ftxt.write('    }\n')
                ftxt.write('  ],\n')
        elif prj_info.line_num == 1002:
            with open(write_path, 'a') as ftxt:
                ftxt.write('  overallInfo: [\n')
            for ii in range(len(line)):
                model_acc = float("%.3f" % float(line[ii]))
                model_param = full_model_param[ii] / 10000000.
                model_name = name_list[ii]
                if ii == len(line) - 1:
                    info = '    [[' + str(model_param) + ', ' + str(model_acc) + ', ' + '\'' + model_name + '\']]\n'
                else:
                    info = '    [[' + str(model_param) + ', ' + str(model_acc) + ', ' + '\'' + model_name + '\']],\n'
                with open(write_path, 'a') as ftxt:
                    ftxt.write(info)
            with open(write_path, 'a') as ftxt:
                ftxt.write('  ]\n')
                ftxt.write('}\n')
        else:
            print('wrong!')