import os
import numpy as np
from utils import task2ImgGet, getRGBhist

exampleModel = 'resnet152'
dataset_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'dataset')
output_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'exp_out')
rgb_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'rgb_out')
exp_name3 = 'smoothgradcampp_cam'
# task2ImgGet(dataset_path, exampleModel)
out_path = os.path.join(dataset_path, 'ImageNet_Val', 'task2_info', f'model.{exampleModel}')
example_names = np.load(os.path.join(out_path, 'task2examplenameTotal.npy')).tolist()

i = 0
for img_name in example_names[0:1500]:
    hist = getRGBhist(dataset_path, img_name, output_path, rgb_path, exampleModel, exp_name3)
    i += 1
    print(f'hist generation: {i} / {len(example_names[0:1500])}')