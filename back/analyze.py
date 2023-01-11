import os
import csv
import pandas as pd
import numpy as np
from scipy import stats

dataset_path = os.path.join(os.path.dirname(
    os.path.dirname(os.getcwd())), 'dataset')
model_list = [
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

csv_path0 = os.path.join(dataset_path, 'ImageNet_Val', 'accuracy_0.csv')
csv_path1 = os.path.join(dataset_path, 'ImageNet_Val', 'accuracy_1.csv')
csv_path2 = os.path.join(dataset_path, 'ImageNet_Val', 'accuracy_2.csv')
csv_path3 = os.path.join(dataset_path, 'ImageNet_Val', 'accuracy_3.csv')


# line  = ['model']
# for i in range(1000):
#     line.append(f'label_{i}')
# with open(csv_path0, 'a') as f:
#     writer = csv.writer(f)
#     writer.writerow(line)

# for model_name in model_list:
#     row = []
#     row.append(model_name)
#     accuracy_list = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{model_name}', 'accuracy.npy')).tolist()
#     del accuracy_list[1000]
#     row.extend(accuracy_list)
#     with open(csv_path0, 'a') as f:
#         writer = csv.writer(f)
#         writer.writerow(row)

# df = pd.read_csv(csv_path0)
# df.values
# data = df.as_matrix()
# data = list(map(list,zip(*data)))
# data = pd.DataFrame(data)
# data.to_csv(csv_path1, header=0, index=0)


# with open(csv_path1, 'r') as f:
#     prj_info = csv.reader(f)
#     for row in prj_info:
#         if prj_info.line_num == 1:
#             write_info = ['label']
#             write_info.append('max')
#             write_info.append('min')
#             write_info.append('max-min')
#             write_info.append('mean')
#             write_info.append('median')
#             write_info.append('mode')
#             with open(csv_path2, 'a') as f:
#                 writer = csv.writer(f)
#                 writer.writerow(write_info)
#         else:
#             cur_label = prj_info.line_num - 2
#             labelAccuracy = []
#             for i in range(len(row)):
#                 labelAccuracy.append(float(row[i]))
#             write_info = [f'label_{cur_label}']
#             write_info.append(max(labelAccuracy))
#             write_info.append(min(labelAccuracy))
#             write_info.append(max(labelAccuracy) - min(labelAccuracy))
#             write_info.append(np.mean(labelAccuracy))
#             write_info.append(np.median(labelAccuracy))
#             write_info.append(stats.mode(labelAccuracy)[0][0])
#             with open(csv_path2, 'a') as f:
#                 writer = csv.writer(f)
#                 writer.writerow(write_info)

# df = pd.read_csv(csv_path2)
# df.values
# data = df.as_matrix()
# data = list(map(list,zip(*data)))
# data = pd.DataFrame(data)
# data.to_csv(csv_path3, header=0, index=0)

with open(csv_path0, 'r') as f:
    prj_info = csv.reader(f)
    for row in prj_info:
        if prj_info.line_num == 14:
            print(row[0])
            del row[0]
            info = []
            print('\t', len(row))
            for i in range(len(row)):
                if float(row[i]) < 16:
                    print(i, float(row[i]))
                    # info.append(float(row[i]))
                    # info.append(i)
            # print(info)
            # print('\t', min(info), max(info))

# with open(csv_path3, 'r') as f:
#     prj_info = csv.reader(f)
#     for row in prj_info:
#         # print(row[124])
#         if prj_info.line_num == 5:
#             print(len(row))
#             info = []
#             for i in range(len(row)):
#                 info.append(float(row[i]))
#                 if float(row[i]) > 97:
#                     print('max-min>97', i, float(row[i]))
                # if float(row[i]) > 97:
                #     print('max-min>97', i, float(row[i]))
            # print(max(info))
            # print(min(info))

# with open(csv_path, 'r') as f:
#     prj_info = csv.reader(f)
#     for row in prj_info:
#       if prj_info.line_num != 1:
#         print(f'{row[0]}:')
#         overall_acc = float(row[1001])
#         label_acc = row[1: 1001]
#         label_accs = []
#         for acc in label_acc:
#           label_accs.append(float(acc))
#         label_accs = np.array(label_accs)

#         diff_label_acc = label_accs - overall_acc
#         label_range = range(1000)
#         plt.figure()
#         plt.plot(label_range, diff_label_acc)
#         plt.xlabel('label')
#         plt.ylabel('(label accuracy) - (overall accuracy)')
#         plt.title(f'{row[0]} overall accuracy: {overall_acc}%')
#         plt.savefig(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'dataset', 'ImageNet_Val', 'plots', f'model.{row[0]}_diff.JPEG'))
#         plt.close()

# a = np.array([1, 4, 3, 5, 2, 5, 6, 6])
# b = np.argsort(a)
# print(b)
# for i in range(len(b)):
#     a[b[i]] = i
# print(a)

# with open(csv_path_1, 'r') as f:
#     prj_info = csv.reader(f)
#     for row in prj_info:
        