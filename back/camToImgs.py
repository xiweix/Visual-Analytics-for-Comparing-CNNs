import os
import numpy as np
from scorecam_utils import scorecam_to_img
from gradcam_utils import cam_to_img
from smooth_utils.visualize import smoothcam_to_img

dataset_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'dataset')
output_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'exp_out')
os.makedirs(output_path, exist_ok=True)
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
example_names = np.load(os.path.join(dataset_path, 'name.npy')).tolist()
model_name = full_model_list[2]
for image_name in example_names:
    scorecam_to_img(dataset_path, image_name, model_name, output_path)

    cam_to_img(dataset_path, image_name, model_name, output_path)

    smoothcam_to_img(dataset_path, image_name, model_name, output_path)