import os
import numpy as np
import skimage.transform
import torch
import torch.nn as nn
import torch.nn. functional as F

from PIL import Image
import matplotlib.pyplot as plt
from torchvision import models, transforms
from torchvision.utils import save_image

from smoothgradcam import CAM, GradCAM, GradCAMpp, SmoothGradCAMpp
from smooth_utils.visualize import visualize, reverse_normalize, smoothcam_to_img
from smooth_utils.imagenet_labels import label2idx, idx2label

def smooth_main(dataset_path, image_name, model_name, output_path):
    useCUDA = torch.cuda.is_available()
    torch.cuda.empty_cache()
    # if not os.path.exists(os.path.join(output_dir, f'{model_name}_smoothgradcampp_cam.npy')):
    cam_dict = dict()

    model = getattr(models, model_name)(pretrained=True)
    model.eval()
    if useCUDA:
        model.cuda()
    if model_name == 'mobilenet_v2':
        # target_layer = model.features[18][0]
        target_layer = model.features[18][2]
    elif model_name == 'alexnet':
        # target_layer = model.features[10]
        target_layer = model.features[11]
    elif model_name == 'resnet18':
        # target_layer = model.layer4[1].conv2
        target_layer = model.layer4[1].bn2
    elif model_name == 'resnet34':
        # target_layer = model.layer4[2].conv2
        target_layer = model.layer4[2].bn2
    elif model_name == 'resnet50' or model_name == 'resnet101' or model_name == 'resnet152':
        # target_layer = model.layer4[2].conv3
        target_layer = model.layer4[2]
    elif model_name == 'densenet121':
        # target_layer = model.features.denseblock4.denselayer16.conv2
        target_layer = model.features.norm5
    elif model_name == 'densenet161':
        # target_layer = model.features.denseblock4.denselayer24.conv2
        target_layer = model.features.norm5
    elif model_name == 'densenet169' or model_name == 'densenet201':
        # target_layer = model.features.denseblock4.denselayer32.conv2
        target_layer = model.features.norm5
    elif model_name == 'squeezenet1_1':
        # target_layer = model.features[12].expand3x3
        target_layer = model.features[12].expand3x3_activation
    elif model_name == 'shufflenet_v2_x0_5':
        # target_layer = model.conv5[0]
        target_layer = model.conv5[2]
    # print(model_name, ':', target_layer)

    # wrapper for class activation mapping. Choose one of the following.
    # wrapped_model = CAM(model, target_layer)
    # wrapped_model =GradCAM(model, target_layer)
    # wrapped_model = GradCAMpp(model, target_layer)

    # process image
    img_path = os.path.join(dataset_path, 'ILSVRC2012_img_val', image_name)
    image = Image.open(img_path).convert('RGB')
    base_name = os.path.splitext(image_name)[0]
    output_dir = os.path.join(output_path, base_name)
    os.makedirs(output_dir, exist_ok=True)
    normalize = transforms.Normalize(
      mean=[0.485, 0.456, 0.406],
      std=[0.229, 0.224, 0.225]
    )
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        normalize
    ])
    # convert image to tensor
    tensor = preprocess(image)

    # reshape 4D tensor (N, C, H, W)
    tensor = tensor.unsqueeze(0)
    if useCUDA:
        tensor = tensor.cuda()

    wrapped_model = SmoothGradCAMpp(model, target_layer, n_samples=25, stdev_spread=0.15)

    cam, idx = wrapped_model(tensor)
    cam = cam.cpu()
    # print(idx2label[idx])
    img = reverse_normalize(tensor)
    # plt.imshow(cam.squeeze().numpy(), alpha=0.5, cmap='jet')
    # save_image(cam, os.path.join(output_dir, f'{model_name}_smoothgradcampp_sq.JPEG'))
    visualize(img, cam, output_dir, model_name)

    # else:
    #     smoothcam_to_img(dataset_path, image_name, model_name, output_dir)