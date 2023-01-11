#!/usr/bin/env python
# coding: utf-8
#
# Author:   Kazuto Nakashima
# URL:      http://kazuto1011.github.io
# Created:  2017-05-18

from __future__ import print_function

import copy
import os

import click
import cv2
import matplotlib.cm as cm
import numpy as np
import torch
import torch.nn.functional as F
from torchvision import models, transforms

from multi_grad import (
    BackPropagation,
    Deconvnet,
    GradCAM,
    GuidedBackPropagation,
    occlusion_sensitivity,
)

# if a model includes LSTM, such as in image captioning,
# torch.backends.cudnn.enabled = False


def get_device(cuda):
    cuda = cuda and torch.cuda.is_available()
    device = torch.device("cuda" if cuda else "cpu")
    if cuda:
        current_device = torch.cuda.current_device()
        print("Device:", torch.cuda.get_device_name(current_device))
    else:
        print("Device: CPU")
    return device


def load_images(image_names, dataset_path, output_path, model_name):
    images = []
    raw_images = []
    output_dirs = []
    exist_res = 0
    for i, image_name in enumerate(image_names):
        image_path = os.path.join(dataset_path, 'ILSVRC2012_img_val', image_name)
        output_dir = os.path.join(output_path, os.path.splitext(image_name)[0])
        os.makedirs(output_dir, exist_ok=True)
        if os.path.exists(os.path.join(output_dir,f"{model_name}_vanilla.JPEG")) and os.path.exists(os.path.join(output_dir, f"{model_name}_deconvnet.JPEG")) and os.path.exists(os.path.join(output_dir, f"{model_name}_guided_backprop.JPEG")):
            exist_res += 1
        else:
            print("Images:")
            print(f"\t#{i}: {image_name}")
            image, raw_image = preprocess(image_path)
            images.append(image)
            raw_images.append(raw_image)
            output_dirs.append(output_dir)
    return images, raw_images, output_dirs, exist_res


def get_classtable(synset_word_file):
    classes = []
    with open(synset_word_file) as lines:
        for line in lines:
            line = line.strip().split(" ", 1)[1]
            line = line.split(", ", 1)[0].replace(" ", "_")
            classes.append(line)
    return classes


def preprocess(image_path):
    raw_image = cv2.imread(image_path)
    raw_image = cv2.resize(raw_image, (224,) * 2)
    image = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )(raw_image[..., ::-1].copy())
    return image, raw_image


def save_gradient(filename, gradient):
    gradient = gradient.cpu().numpy().transpose(1, 2, 0)
    gradient -= gradient.min()
    gradient /= gradient.max()
    gradient *= 255.0
    cv2.imwrite(filename, np.uint8(gradient))


def save_gradcam(filename, gcam, raw_image, paper_cmap=False):
    gcam = gcam.cpu().numpy()
    cmap = cm.jet_r(gcam)[..., :3] * 255.0
    if paper_cmap:
        alpha = gcam[..., None]
        gcam = alpha * cmap + (1 - alpha) * raw_image
    else:
        gcam = (cmap.astype(np.float) + raw_image.astype(np.float)) / 2
    cv2.imwrite(filename, np.uint8(gcam))


def save_sensitivity(filename, maps):
    maps = maps.cpu().numpy()
    scale = max(maps[maps > 0].max(), -maps[maps <= 0].min())
    maps = maps / scale * 0.5
    maps += 0.5
    maps = cm.bwr_r(maps)[..., :3]
    maps = np.uint8(maps * 255.0)
    maps = cv2.resize(maps, (224, 224), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite(filename, maps)


def demo1(dataset_path, image_names, model_name, output_path, input_label, explain_methods):
    """
    Visualize model responses given multiple images
    """
    # topk = 1
    cuda = True
    # synset_word_file = os.path.join(dataset_path, 'synset_words.txt')

    # if 'resnet' in model_name:
    #     target_layer = 'layer4'
    # elif 'densenet' in model_name:
    #     target_layer = 'features.norm5'
    # elif 'alexnet' in model_name:
    #     target_layer = 'features.12'
    # elif 'squeezenet' in model_name:
    #     target_layer = 'features.12'
    # elif 'shufflenet' in model_name:
    #     target_layer = 'conv5.2'
    # elif 'mobilenet' in model_name:
    #     target_layer = 'features.18.2'


    device = get_device(cuda)

    # Synset words
    # classes = get_classtable(synset_word_file)

    # Model from torchvision
    model = getattr(models, model_name)(pretrained=True)
    model.to(device)
    model.eval()

    # Images
    images, _, output_dirs, exist_res = load_images(image_names, dataset_path, output_path, model_name)
    if len(images) != 0:
        images = torch.stack(images).to(device)

    """
    Common usage:
    1. Wrap your model with visualization classes defined in grad_cam.py
    2. Run forward() with images
    3. Run backward() with a list of specific classes
    4. Run generate() to export results
    """
    # print(model_name)
    # =========================================================================
    # print("Vanilla Backpropagation")

    if 'Vanilla Backpropagation' in explain_methods and len(images) != 0:
        bp = BackPropagation(model=model)
        _, ids = bp.forward(images)  # sorted

        # idd = torch.full((len(image_names), 1), input_label).cuda()

        # for i in range(topk):
        bp.backward(ids=ids[:, [0]])
        # bp.backward(ids=idd)

        gradients = bp.generate()

        # Save results as image files
        for j in range(len(images)):
            # print("\t#{}: {} ({:.5f})".format(j, classes[ids[j, i]], probs[j, i]))

            save_gradient(
                filename=os.path.join(output_dirs[j],f"{model_name}_vanilla.JPEG"),
                gradient=gradients[j],
            )

        # Remove all the hook function in the "model"
        bp.remove_hook()

    # =========================================================================
    # print("Deconvolution")

    if 'Deconvolution' in explain_methods and len(images) != 0:
        deconv = Deconvnet(model=model)
        _ = deconv.forward(images)

        # for i in range(topk):
        deconv.backward(ids=ids[:, [0]])
        # deconv.backward(ids=idd)

        gradients = deconv.generate()

        for j in range(len(images)):
            # print("\t#{}: {} ({:.5f})".format(j, classes[ids[j, i]], probs[j, i]))

            save_gradient(
                filename=os.path.join(output_dirs[j], f"{model_name}_deconvnet.JPEG"),
                gradient=gradients[j],
            )

        deconv.remove_hook()

    # =========================================================================
    # print("Guided Backpropagation")

    # gcam = GradCAM(model=model)
    # _ = gcam.forward(images)

    if 'Guided Backpropagation' in explain_methods and len(images) != 0:
        gbp = GuidedBackPropagation(model=model)
        _ = gbp.forward(images)

        # for i in range(topk):
        # Guided Backpropagation
        gbp.backward(ids=ids[:, [0]])
        # gbp.backward(ids=idd)

        gradients = gbp.generate()

        # # Grad-CAM
        # gcam.backward(ids=ids[:, [i]])
        # regions = gcam.generate(target_layer=target_layer)

        for j in range(len(images)):
            # print("\t#{}: {} ({:.5f})".format(j, classes[ids[j, i]], probs[j, i]))

            # Guided Backpropagation
            save_gradient(
                filename=os.path.join(output_dirs[j], f"{model_name}_guided_backprop.JPEG"),
                gradient=gradients[j],
            )

        # # Grad-CAM
        # save_gradcam(
        #     filename=os.path.join(
        #         output_dir,
        #         "{}-{}-gradcam-{}-{}.JPEG".format(
        #             j, model_name, target_layer, classes[ids[j, i]]
        #         ),
        #     ),
        #     gcam=regions[j, 0],
        #     raw_image=raw_images[j],
        # )

        # # Guided Grad-CAM
        # save_gradient(
        #     filename=os.path.join(
        #         output_dirs[j],
        #         "{}_guided_gradcam.JPEG".format(model_name),
        #     ),
        #     gradient=torch.mul(regions, gradients)[j],
        # )
    print(f'Input {len(image_names)} images, {exist_res} already exists, generate {len(output_dirs)} this time')
