# grad-CAM and grad-CAM++, part of the code is from:
# https://github.com/1Konny/gradcam_plus_plus-pytorch/blob/master/gradcam.py

import os
import warnings
import numpy as np
import PIL
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
from torchvision import transforms
from torchvision.utils import make_grid, save_image
from gradcam_utils import visualize_cam, Normalize
from gradcam import GradCAM, GradCAMpp

warnings.filterwarnings("ignore")

def gradcamMain(model_list, img_name_list, dataset_path, output_path):
    use_cuda = torch.cuda.is_available()
    # use_cuda = False
    # Load torchvision models and make model dictionaries
    cam_dict = dict()

    if 'alexnet' in model_list:
        alexnet = models.alexnet(pretrained=True)
        alexnet.eval()
        if use_cuda == True:
            alexnet.cuda()
        alexnet_model_dict = dict(type='alexnet', arch=alexnet,
                                layer_name='features_11', input_size=(224, 224))
        # alexnet_model_dict = dict(type='alexnet', arch=alexnet,
        #                         layer_name='features_10', input_size=(224, 224))
        alexnet_gradcam = GradCAM(alexnet_model_dict, True)
        alexnet_gradcampp = GradCAMpp(alexnet_model_dict, True)
        cam_dict['alexnet'] = [alexnet_gradcam, alexnet_gradcampp]

    if 'vgg11' in model_list:
        vgg11 = models.vgg11(pretrained=True)
        vgg11.eval()
        if use_cuda == True:
            vgg11.cuda()
        vgg11_model_dict = dict(type='vgg11', arch=vgg11,
                                layer_name='features_19', input_size=(224, 224))
        vgg11_gradcam = GradCAM(vgg11_model_dict, True)
        vgg11_gradcampp = GradCAMpp(vgg11_model_dict, True)
        cam_dict['vgg11'] = [vgg11_gradcam, vgg11_gradcampp]

    if 'vgg13' in model_list:
        vgg13 = models.vgg13(pretrained=True)
        vgg13.eval()
        if use_cuda == True:
            vgg13.cuda()
        vgg13_model_dict = dict(type='vgg13', arch=vgg13,
                                layer_name='features_23', input_size=(224, 224))
        vgg13_gradcam = GradCAM(vgg13_model_dict, True)
        vgg13_gradcampp = GradCAMpp(vgg13_model_dict, True)
        cam_dict['vgg13'] = [vgg13_gradcam, vgg13_gradcampp]

    if 'vgg16' in model_list:
        vgg16 = models.vgg16(pretrained=True)
        vgg16.eval()
        if use_cuda == True:
            vgg16.cuda()
        vgg16_model_dict = dict(type='vgg16', arch=vgg16,
                                layer_name='features_29', input_size=(224, 224))
        vgg16_gradcam = GradCAM(vgg16_model_dict, True)
        vgg16_gradcampp = GradCAMpp(vgg16_model_dict, True)
        cam_dict['vgg16'] = [vgg16_gradcam, vgg16_gradcampp]

    if 'vgg19' in model_list:
        vgg19 = models.vgg19(pretrained=True)
        vgg19.eval()
        if use_cuda == True:
            vgg19.cuda()
        vgg19_model_dict = dict(type='vgg19', arch=vgg19,
                                layer_name='features_35', input_size=(224, 224))
        vgg19_gradcam = GradCAM(vgg19_model_dict, True)
        vgg19_gradcampp = GradCAMpp(vgg19_model_dict, True)
        cam_dict['vgg19'] = [vgg19_gradcam, vgg19_gradcampp]

    if 'resnet18' in model_list:
        resnet18 = models.resnet18(pretrained=True)
        resnet18.eval()
        if use_cuda == True:
            resnet18.cuda()
        resnet18_model_dict = dict(type='resnet18', arch=resnet18,
                                layer_name='layer4', input_size=(224, 224))
        # resnet18_model_dict = dict(type='resnet18', arch=resnet18,
        #                         layer_name='layer4_1_conv2', input_size=(224, 224))
        resnet18_gradcam = GradCAM(resnet18_model_dict, True)
        resnet18_gradcampp = GradCAMpp(resnet18_model_dict, True)
        cam_dict['resnet18'] = [resnet18_gradcam, resnet18_gradcampp]

    if 'resnet34' in model_list:
        resnet34 = models.resnet34(pretrained=True)
        resnet34.eval()
        if use_cuda == True:
            resnet34.cuda()
        resnet34_model_dict = dict(type='resnet34', arch=resnet34,
                                layer_name='layer4', input_size=(224, 224))
        # resnet34_model_dict = dict(type='resnet34', arch=resnet34,
        #                         layer_name='layer4_2_conv2', input_size=(224, 224))
        resnet34_gradcam = GradCAM(resnet34_model_dict, True)
        resnet34_gradcampp = GradCAMpp(resnet34_model_dict, True)
        cam_dict['resnet34'] = [resnet34_gradcam, resnet34_gradcampp]

    if 'resnet50' in model_list:
        resnet50 = models.resnet50(pretrained=True)
        resnet50.eval()
        if use_cuda == True:
            resnet50.cuda()
        resnet50_model_dict = dict(type='resnet50', arch=resnet50,
                                layer_name='layer4', input_size=(224, 224))
        # resnet50_model_dict = dict(type='resnet50', arch=resnet50,
        #                         layer_name='layer4_2_conv3', input_size=(224, 224))
        resnet50_gradcam = GradCAM(resnet50_model_dict, True)
        resnet50_gradcampp = GradCAMpp(resnet50_model_dict, True)
        cam_dict['resnet50'] = [resnet50_gradcam, resnet50_gradcampp]

    if 'resnet101' in model_list:
        resnet101 = models.resnet101(pretrained=True)
        resnet101.eval()
        if use_cuda == True:
            resnet101.cuda()
        resnet101_model_dict = dict(type='resnet101', arch=resnet101,
                                    layer_name='layer4', input_size=(224, 224))
        # resnet101_model_dict = dict(type='resnet101', arch=resnet101,
        #                             layer_name='layer4_2_conv3', input_size=(224, 224))
        resnet101_gradcam = GradCAM(resnet101_model_dict, True)
        resnet101_gradcampp = GradCAMpp(resnet101_model_dict, True)
        cam_dict['resnet101'] = [resnet101_gradcam, resnet101_gradcampp]

    if 'resnet152' in model_list:
        resnet152 = models.resnet152(pretrained=True)
        resnet152.eval()
        if use_cuda == True:
            resnet152.cuda()
        resnet152_model_dict = dict(type='resnet152', arch=resnet152,
                                    layer_name='layer4', input_size=(224, 224))
        # resnet152_model_dict = dict(type='resnet152', arch=resnet152,
        #                             layer_name='layer4_2_conv3', input_size=(224, 224))
        resnet152_gradcam = GradCAM(resnet152_model_dict, True)
        resnet152_gradcampp = GradCAMpp(resnet152_model_dict, True)
        cam_dict['resnet152'] = [resnet152_gradcam, resnet152_gradcampp]

    if 'densenet121' in model_list:
        densenet121 = models.densenet121(pretrained=True)
        densenet121.eval()
        if use_cuda == True:
            densenet121.cuda()
        densenet121_model_dict = dict(type='densenet121', arch=densenet121,
                                    layer_name='features_norm5', input_size=(224, 224))
        # densenet121_model_dict = dict(type='densenet121', arch=densenet121,
        #                             layer_name='features_denseblock4_denselayer16_conv2', input_size=(224, 224))
        densenet121_gradcam = GradCAM(densenet121_model_dict, True)
        densenet121_gradcampp = GradCAMpp(densenet121_model_dict, True)
        cam_dict['densenet121'] = [densenet121_gradcam, densenet121_gradcampp]

    if 'densenet161' in model_list:
        densenet161 = models.densenet161(pretrained=True)
        densenet161.eval()
        if use_cuda == True:
            densenet161.cuda()
        densenet161_model_dict = dict(type='densenet161', arch=densenet161,
                                    layer_name='features_norm5', input_size=(224, 224))
        # densenet161_model_dict = dict(type='densenet161', arch=densenet161,
        #                             layer_name='features_denseblock4_denselayer24_conv2', input_size=(224, 224))
        densenet161_gradcam = GradCAM(densenet161_model_dict, True)
        densenet161_gradcampp = GradCAMpp(densenet161_model_dict, True)
        cam_dict['densenet161'] = [densenet161_gradcam, densenet161_gradcampp]

    if 'densenet169' in model_list:
        densenet169 = models.densenet169(pretrained=True)
        densenet169.eval()
        if use_cuda == True:
            densenet169.cuda()
        densenet169_model_dict = dict(type='densenet169', arch=densenet169,
                                    layer_name='features_norm5', input_size=(224, 224))
        # densenet169_model_dict = dict(type='densenet169', arch=densenet169,
        #                             layer_name='features_denseblock4_denselayer32_conv2', input_size=(224, 224))
        densenet169_gradcam = GradCAM(densenet169_model_dict, True)
        densenet169_gradcampp = GradCAMpp(densenet169_model_dict, True)
        cam_dict['densenet169'] = [densenet169_gradcam, densenet169_gradcampp]

    if 'densenet201' in model_list:
        densenet201 = models.densenet201(pretrained=True)
        densenet201.eval()
        if use_cuda == True:
            densenet201.cuda()
        densenet201_model_dict = dict(type='densenet201', arch=densenet201,
                                    layer_name='features_norm5', input_size=(224, 224))
        # densenet201_model_dict = dict(type='densenet201', arch=densenet201,
        #                             layer_name='features_denseblock4_denselayer32_conv2', input_size=(224, 224))
        densenet201_gradcam = GradCAM(densenet201_model_dict, True)
        densenet201_gradcampp = GradCAMpp(densenet201_model_dict, True)
        cam_dict['densenet201'] = [densenet201_gradcam, densenet201_gradcampp]

    if 'squeezenet1_1' in model_list:
        squeezenet1_1 = models.squeezenet1_1(pretrained=True)
        squeezenet1_1.eval()
        if use_cuda == True:
            squeezenet1_1.cuda()
        squeezenet1_1_model_dict = dict(type='squeezenet1_1', arch=squeezenet1_1,
                                        layer_name='features_12', input_size=(224, 224))
        # squeezenet1_1_model_dict = dict(type='squeezenet1_1', arch=squeezenet1_1,
        #                                 layer_name='classifier_1', input_size=(224, 224))
        squeezenet1_1_gradcam = GradCAM(squeezenet1_1_model_dict, True)
        squeezenet1_1_gradcampp = GradCAMpp(squeezenet1_1_model_dict, True)
        cam_dict['squeezenet1_1'] = [
            squeezenet1_1_gradcam, squeezenet1_1_gradcampp]

    if 'mobilenet_v2' in model_list:
        mobilenet_v2 = models.mobilenet_v2(pretrained=True)
        mobilenet_v2.eval()
        if use_cuda == True:
            mobilenet_v2.cuda()
        mobilenet_v2_model_dict = dict(type='mobilenet_v2', arch=mobilenet_v2,
                                    layer_name='features_18', input_size=(224, 224))
        # mobilenet_v2_model_dict = dict(type='mobilenet_v2', arch=mobilenet_v2,
        #                             layer_name='features_18_0', input_size=(224, 224))
        mobilenet_v2_gradcam = GradCAM(mobilenet_v2_model_dict, True)
        mobilenet_v2_gradcampp = GradCAMpp(mobilenet_v2_model_dict, True)
        cam_dict['mobilenet_v2'] = [
            mobilenet_v2_gradcam, mobilenet_v2_gradcampp]

    if 'shufflenet_v2_x0_5' in model_list:
        shufflenet_v2_x0_5 = models.shufflenet_v2_x0_5(pretrained=True)
        shufflenet_v2_x0_5.eval()
        if use_cuda == True:
            shufflenet_v2_x0_5.cuda()
        shufflenet_v2_x0_5_model_dict = dict(
            type='shufflenet_v2_x0_5', arch=shufflenet_v2_x0_5, layer_name='conv5', input_size=(224, 224))
        # shufflenet_v2_x0_5_model_dict = dict(
        #     type='shufflenet_v2_x0_5', arch=shufflenet_v2_x0_5, layer_name='conv5_0', input_size=(224, 224))
        shufflenet_v2_x0_5_gradcam = GradCAM(
            shufflenet_v2_x0_5_model_dict, True)
        shufflenet_v2_x0_5_gradcampp = GradCAMpp(
            shufflenet_v2_x0_5_model_dict, True)
        cam_dict['shufflenet_v2_x0_5'] = [
            shufflenet_v2_x0_5_gradcam, shufflenet_v2_x0_5_gradcampp]

    if 'shufflenet_v2_x1_0' in model_list:
        shufflenet_v2_x1_0 = models.shufflenet_v2_x1_0(pretrained=True)
        shufflenet_v2_x1_0.eval()
        if use_cuda == True:
            shufflenet_v2_x1_0.cuda()
        shufflenet_v2_x1_0_model_dict = dict(
            type='shufflenet_v2_x1_0', arch=shufflenet_v2_x1_0, layer_name='conv5', input_size=(224, 224))
        shufflenet_v2_x1_0_gradcam = GradCAM(
            shufflenet_v2_x1_0_model_dict, True)
        shufflenet_v2_x1_0_gradcampp = GradCAMpp(
            shufflenet_v2_x1_0_model_dict, True)
        cam_dict['shufflenet_v2_x1_0'] = [
            shufflenet_v2_x1_0_gradcam, shufflenet_v2_x1_0_gradcampp]
    j = 0
    for img_name in img_name_list:
        # print(vis_method, img_name)
        # Load image
        img_dir = os.path.join(dataset_path, 'ILSVRC2012_img_val')
        img_path = os.path.join(img_dir, img_name)
        pil_img = PIL.Image.open(img_path).convert('RGB')

        # define the output direction
        base_name = os.path.splitext(img_name)[0]
        output_dir = os.path.join(output_path, base_name)
        os.makedirs(output_dir, exist_ok=True)

        # preprocess image
        normalizer = Normalize(mean=[0.485, 0.456, 0.406], std=[
                            0.229, 0.224, 0.225])
        torch_img = torch.from_numpy(np.asarray(pil_img)).permute(
            2, 0, 1).unsqueeze(0).float().div(255)
        if use_cuda == True:
            torch_img = torch_img.cuda()
        torch_img = F.upsample(torch_img, size=(224, 224),
                            mode='bilinear', align_corners=False)
        normed_torch_img = normalizer(torch_img)

        # Feedforward image, calculate GradCAM/GradCAM++, and gather results
        i = 0
        for gradcam, gradcam_pp in cam_dict.values():
            model_name = list(cam_dict)[i]
            # print(model_name)
            if not os.path.exists(os.path.join(output_dir, f'{model_name}_gradcampp.png')):
                mask, _ = gradcam(normed_torch_img)
                mask = np.uint8(255 * mask.squeeze().cpu())
                np.save(os.path.join(output_dir, f'{model_name}_gradcam_mask.npy'), mask)

                heatmap, result = visualize_cam(mask, torch_img)
                save_image(heatmap, os.path.join(
                    output_dir, f'{model_name}_gradcam.png'))
                save_image(result, os.path.join(
                    output_dir, f'{model_name}_gradcam_img.png'))

                # elif vis_method == 'Grad-CAM++' and not os.path.exists(os.path.join(output_dir, f'{model_name}_gradcampp.png')):
                # elif vis_method == 'Grad-CAM++':
                mask_pp, _ = gradcam_pp(normed_torch_img)
                mask_pp = np.uint8(255 * mask_pp.squeeze().cpu())
                np.save(os.path.join(output_dir, f'{model_name}_gradcampp_mask.npy'), mask_pp)

                heatmap_pp, result_pp = visualize_cam(mask_pp, torch_img)
                save_image(heatmap_pp, os.path.join(
                    output_dir, f'{model_name}_gradcampp.png'))
                save_image(result_pp, os.path.join(
                    output_dir, f'{model_name}_gradcampp_img.png'))
            i += 1
            # print('regenerate')
        j += 1
        print(f'gradcam {img_name} {j}/{len(img_name_list)}')