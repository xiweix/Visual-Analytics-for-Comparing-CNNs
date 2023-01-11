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


def smooth_main(dataset_path, img_name_list, model_list, output_path):
    useCUDA = torch.cuda.is_available()
    torch.cuda.empty_cache()
    # if not os.path.exists(os.path.join(output_dir, f'{model_name}_smoothgradcampp_cam.npy')):
    cam_dict = dict()
    # if 'resnet152ly40' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer4[0]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly40'] = wrapped_model
    # if 'resnet152ly41' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer4[1]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly41'] = wrapped_model
    # if 'resnet152ly42' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer4[2]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly42'] = wrapped_model
    # if 'resnet152ly30' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer3[0]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly30'] = wrapped_model
    # if 'resnet152ly31' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer3[1]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly31'] = wrapped_model
    # if 'resnet152ly32' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer3[2]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly32'] = wrapped_model
    # if 'resnet152ly33' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer3[3]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly33'] = wrapped_model
    # if 'resnet152ly34' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer3[4]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly34'] = wrapped_model
    # if 'resnet152ly35' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer3[5]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly35'] = wrapped_model
    # if 'resnet152ly36' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer3[6]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly36'] = wrapped_model
    # if 'resnet152ly37' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer3[7]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly37'] = wrapped_model
    # if 'resnet152ly38' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer3[8]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly38'] = wrapped_model
    # if 'resnet152ly39' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer3[9]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly39'] = wrapped_model
    # if 'resnet152ly310' in model_list:
    #     resnet152 = getattr(models, 'resnet152')(pretrained=True)
    #     resnet152.eval()
    #     if useCUDA:
    #         resnet152.cuda()
    #     target_layer = resnet152.layer3[10]
    #     wrapped_model = SmoothGradCAMpp(
    #         resnet152, target_layer, n_samples=25, stdev_spread=0.15)
    #     cam_dict['resnet152ly310'] = wrapped_model





    if 'mobilenet_v2' in model_list:
        mobilenet_v2 = getattr(models, 'mobilenet_v2')(pretrained=True)
        mobilenet_v2.eval()
        if useCUDA:
            mobilenet_v2.cuda()
        target_layer = mobilenet_v2.features[18][2]
        wrapped_model = SmoothGradCAMpp(
            mobilenet_v2, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['mobilenet_v2'] = wrapped_model

    if 'alexnet' in model_list:
        alexnet = getattr(models, 'alexnet')(pretrained=True)
        alexnet.eval()
        if useCUDA:
            alexnet.cuda()
        target_layer = alexnet.features[11]
        wrapped_model = SmoothGradCAMpp(
            alexnet, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['alexnet'] = wrapped_model

    if 'resnet18' in model_list:
        resnet18 = getattr(models, 'resnet18')(pretrained=True)
        resnet18.eval()
        if useCUDA:
            resnet18.cuda()
        target_layer = resnet18.layer4[1].bn2
        wrapped_model = SmoothGradCAMpp(
            resnet18, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['resnet18'] = wrapped_model

    if 'resnet34' in model_list:
        resnet34 = getattr(models, 'resnet34')(pretrained=True)
        resnet34.eval()
        if useCUDA:
            resnet34.cuda()
        target_layer = resnet34.layer4[2].bn2
        wrapped_model = SmoothGradCAMpp(
            resnet34, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['resnet34'] = wrapped_model

    if 'resnet50' in model_list:
        resnet50 = getattr(models, 'resnet50')(pretrained=True)
        resnet50.eval()
        if useCUDA:
            resnet50.cuda()
        target_layer = resnet50.layer4[2]
        wrapped_model = SmoothGradCAMpp(
            resnet50, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['resnet50'] = wrapped_model

    if 'resnet101' in model_list:
        resnet101 = getattr(models, 'resnet101')(pretrained=True)
        resnet101.eval()
        if useCUDA:
            resnet101.cuda()
        target_layer = resnet101.layer4[2]
        wrapped_model = SmoothGradCAMpp(
            resnet101, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['resnet101'] = wrapped_model

    if 'resnet152' in model_list:
        resnet152 = getattr(models, 'resnet152')(pretrained=True)
        resnet152.eval()
        if useCUDA:
            resnet152.cuda()
        target_layer = resnet152.layer4[2]
        wrapped_model = SmoothGradCAMpp(
            resnet152, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['resnet152'] = wrapped_model

    if 'densenet121' in model_list:
        densenet121 = getattr(models, 'densenet121')(pretrained=True)
        densenet121.eval()
        if useCUDA:
            densenet121.cuda()
        target_layer = densenet121.features.norm5
        wrapped_model = SmoothGradCAMpp(
            densenet121, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['densenet121'] = wrapped_model

    if 'densenet161' in model_list:
        densenet161 = getattr(models, 'densenet161')(pretrained=True)
        densenet161.eval()
        if useCUDA:
            densenet161.cuda()
        target_layer = densenet161.features.norm5
        wrapped_model = SmoothGradCAMpp(
            densenet161, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['densenet161'] = wrapped_model

    if 'densenet169' in model_list:
        densenet169 = getattr(models, 'densenet169')(pretrained=True)
        densenet169.eval()
        if useCUDA:
            densenet169.cuda()
        target_layer = densenet169.features.norm5
        wrapped_model = SmoothGradCAMpp(
            densenet169, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['densenet169'] = wrapped_model

    if 'densenet201' in model_list:
        densenet201 = getattr(models, 'densenet201')(pretrained=True)
        densenet201.eval()
        if useCUDA:
            densenet201.cuda()
        target_layer = densenet201.features.norm5
        wrapped_model = SmoothGradCAMpp(
            densenet201, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['densenet201'] = wrapped_model

    if 'squeezenet1_1' in model_list:
        squeezenet1_1 = getattr(models, 'squeezenet1_1')(pretrained=True)
        squeezenet1_1.eval()
        if useCUDA:
            squeezenet1_1.cuda()
        target_layer = squeezenet1_1.features[12].expand3x3_activation
        wrapped_model = SmoothGradCAMpp(
            squeezenet1_1, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['squeezenet1_1'] = wrapped_model

    if 'shufflenet_v2_x0_5' in model_list:
        shufflenet_v2_x0_5 = getattr(
            models, 'shufflenet_v2_x0_5')(pretrained=True)
        shufflenet_v2_x0_5.eval()
        if useCUDA:
            shufflenet_v2_x0_5.cuda()
        target_layer = shufflenet_v2_x0_5.conv5[2]
        wrapped_model = SmoothGradCAMpp(
            shufflenet_v2_x0_5, target_layer, n_samples=25, stdev_spread=0.15)
        cam_dict['shufflenet_v2_x0_5'] = wrapped_model

    # wrapper for class activation mapping. Choose one of the following.
    # wrapped_model = CAM(model, target_layer)
    # wrapped_model =GradCAM(model, target_layer)
    # wrapped_model = GradCAMpp(model, target_layer)
    j = 0
    for image_name in img_name_list:
        # process image
        print(f'{model_list} smoothgradcam++ {image_name} {j}/{len(img_name_list)}')

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

        i = 0
        for smoothCAM in cam_dict.values():
            model_name = list(cam_dict)[i]
            # print(model_name)
            # if not os.path.exists(os.path.join(output_dir, f'{model_name}_smoothgradcampp.png')):
            tensor = preprocess(image)
            tensor = tensor.unsqueeze(0)
            if useCUDA:
                tensor = tensor.cuda()
            cam, idx = smoothCAM(tensor)
            cam = cam.cpu()
            # print(idx2label[idx])
            img = reverse_normalize(tensor)
            # plt.imshow(cam.squeeze().numpy(), alpha=0.5, cmap='jet')
            # save_image(cam, os.path.join(output_dir, f'{model_name}_smoothgradcampp_sq.JPEG'))
            visualize(img, cam, output_dir, model_name)
            i += 1
        j += 1
