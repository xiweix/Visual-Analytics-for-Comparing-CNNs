import os
from scorecam_main import scorecamMain
from BBMP import BBMP_process

dataset_path = os.path.join(os.path.dirname(
    os.path.dirname(os.getcwd())), 'dataset')
model_list = [
    'vgg16'
]
output_path = os.path.join(os.path.dirname(
    os.path.dirname(os.getcwd())), 'exp_out')
image_name = 'ILSVRC2012_val_00047809.JPEG'
scorecamMain(['resnet18'], [image_name], dataset_path, output_path)
# image_name = 'ILSVRC2012_val_00027831.JPEG'
# BBMP_process(dataset_path, image_name, 'resnet101', output_path)