import os
import csv

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

write_path = 'modelAccData.txt'
with open(write_path, 'a') as ftxt:
    ftxt.write('export default {\n')
    ftxt.write('  labelAccInfo: [\n')

csv_path = os.path.join(dataset_path, 'ImageNet_Val', 'accuracy_analysis1.csv')
with open(csv_path, 'r') as fcsv:
    prj_info = csv.reader(fcsv)
    for line in prj_info:
        if prj_info.line_num == 1:
            name_list = line
        elif prj_info.line_num < 1001:
            with open(write_path, 'a') as ftxt:
                ftxt.write('    [\n')
            for i in range(len(line)):
                roundNum = ("%.1f" % float(line[i]))
                if i == len(line) - 1:
                    info = '      { name: \'' + name_list[i] + '\', value: ' + roundNum + ' }\n'
                else:
                    info = '      { name: \'' + name_list[i] + '\', value: ' + roundNum + ' },\n'
                with open(write_path, 'a') as ftxt:
                    ftxt.write(info)
            with open(write_path, 'a') as ftxt:
                ftxt.write('    ],\n')
        elif prj_info.line_num == 1001:
            with open(write_path, 'a') as ftxt:
                ftxt.write('    [\n')
            for i in range(len(line)):
                roundNum = ("%.1f" % float(line[i]))
                if i == len(line) - 1:
                    info = '      { name: \'' + name_list[i] + '\', value: ' + roundNum + ' }\n'
                else:
                    info = '      { name: \'' + name_list[i] + '\', value: ' + roundNum + ' },\n'
                with open(write_path, 'a') as ftxt:
                    ftxt.write(info)
            with open(write_path, 'a') as ftxt:
                ftxt.write('    ]\n')
                ftxt.write('  ],\n')
        elif prj_info.line_num == 1002:
            print(line)
            with open(write_path, 'a') as ftxt:
                ftxt.write('  modelAccInfo: [\n')
            for i in range(len(line)):
                roundNum = ("%.3f" % float(line[i]))
                if i == len(line) - 1:
                    info = '    { name: \'' + name_list[i] + '\', value: ' + roundNum + ' }\n'
                else:
                    info = '    { name: \'' + name_list[i] + '\', value: ' + roundNum + ' },\n'
                with open(write_path, 'a') as ftxt:
                    ftxt.write(info)
            with open(write_path, 'a') as ftxt:
                ftxt.write('  ]\n')
                ftxt.write('}\n')
        else:
          print('wrong')
     
