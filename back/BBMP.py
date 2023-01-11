# main code is from https://github.com/jacobgil/pytorch-explain-black-box

import os
import numpy as np
import torch
from torch.autograd import Variable
from torchvision import models
import cv2
import sys


def tv_norm(input, tv_beta):
    img = input[0, 0, :]
    row_grad = torch.mean(torch.abs((img[:-1, :] - img[1:, :])).pow(tv_beta))
    col_grad = torch.mean(torch.abs((img[:, :-1] - img[:, 1:])).pow(tv_beta))
    return row_grad + col_grad


def preprocess_image(img, use_cuda):
    means = [0.485, 0.456, 0.406]
    stds = [0.229, 0.224, 0.225]

    preprocessed_img = img.copy()[:, :, ::-1]
    for i in range(3):
        preprocessed_img[:, :, i] = preprocessed_img[:, :, i] - means[i]
        preprocessed_img[:, :, i] = preprocessed_img[:, :, i] / stds[i]
    preprocessed_img = \
        np.ascontiguousarray(np.transpose(preprocessed_img, (2, 0, 1)))

    if use_cuda:
        preprocessed_img_tensor = torch.from_numpy(preprocessed_img).cuda()
    else:
        preprocessed_img_tensor = torch.from_numpy(preprocessed_img)

    preprocessed_img_tensor.unsqueeze_(0)
    return Variable(preprocessed_img_tensor, requires_grad=False)


def save(mask, img, blurred, model_name, out_path):
    mask = mask.cpu().data.numpy()[0]
    mask = np.transpose(mask, (1, 2, 0))

    mask = (mask - np.min(mask)) / np.max(mask)
    mask = 1 - mask

    np.save(os.path.join(out_path, f"{model_name}_BBMP_mask.npy"), mask)
    heatmap = cv2.applyColorMap(np.uint8(255*mask), cv2.COLORMAP_VIRIDIS)

    heatmap = np.float32(heatmap) / 255
    cam = 1.0*heatmap + np.float32(img)/255
    cam = cam / np.max(cam)

    # img = np.float32(img) / 255
    # perturbated = np.multiply(1 - mask, img) + np.multiply(mask, blurred)

    # cv2.imwrite(os.path.join(out_path, f"{model_name}_perturbated.png"),
    #             np.uint8(255*perturbated))
    cv2.imwrite(os.path.join(out_path, f"{model_name}_BBMP.png"), np.uint8(255*heatmap))
    # cv2.imwrite(os.path.join(out_path, f"{model_name}_mask.png"), np.uint8(255*mask))
    cv2.imwrite(os.path.join(out_path, f"{model_name}_BBMP_img.png"), np.uint8(255*cam))


def BBMPmask_to_heatmap(dataset_path, image_name, model_name, output_path):
    base_name = os.path.splitext(image_name)[0]
    output_dir = os.path.join(output_path, base_name)
    mask = np.load(os.path.join(output_dir, f"{model_name}_BBMP_mask.npy"))

    img_path = os.path.join(dataset_path, 'ILSVRC2012_img_val', image_name)
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224))

    heatmap = cv2.applyColorMap(np.uint8(255*mask), cv2.COLORMAP_VIRIDIS)
    heatmap = np.float32(heatmap) / 255
    cam = 1.0*heatmap + np.float32(img)/255
    cam = cam / np.max(cam)

    cv2.imwrite(os.path.join(output_dir, f"{model_name}_BBMP.png"), np.uint8(255*heatmap))
    cv2.imwrite(os.path.join(output_dir, f"{model_name}_BBMP_img.png"), np.uint8(255*cam))


def numpy_to_torch(img, use_cuda, requires_grad=True):
    if len(img.shape) < 3:
        output = np.float32([img])
    else:
        output = np.transpose(img, (2, 0, 1))

    output = torch.from_numpy(output)
    if use_cuda:
        output = output.cuda()

    output.unsqueeze_(0)
    v = Variable(output, requires_grad=requires_grad)
    return v


def load_model(model_name, use_cuda):
    model = getattr(models, model_name)(pretrained=True)
    model.eval()
    if use_cuda:
        model.cuda()
    if 'alexnet' in model_name or 'vgg' in model_name or 'densenet' in model_name or 'squeezenet' in model_name or 'mobilenet' in model_name:
        for p in model.features.parameters():
            p.requires_grad = False
        for p in model.classifier.parameters():
            p.requires_grad = False
    elif 'resnet' in model_name or 'shufflenet' in model_name or 'googlenet' in model_name or 'inception' in model_name:
        for p in model.parameters():
            p.requires_grad = False
    return model


def BBMP_process(dataset_path, image_name, model_name, output_path):
    # Hyper parameters.
    tv_beta = 3
    learning_rate = 0.1
    max_iterations = 300
    l1_coeff = 0.01
    tv_coeff = 0.2
    use_cuda = torch.cuda.is_available()
    # FloatTensor = torch.cuda.FloatTensor if use_cuda else torch.FloatTensor
    # LongTensor = torch.cuda.LongTensor if use_cuda else torch.LongTensor
    # Tensor = FloatTensor
    base_name = os.path.splitext(image_name)[0]
    out_path = os.path.join(output_path, base_name)

    if not os.path.exists(os.path.join(out_path, f"{model_name}_BBMP.png")):
        img_path = os.path.join(dataset_path, 'ILSVRC2012_img_val', image_name)

        original_img = cv2.imread(img_path)

        original_img = cv2.resize(original_img, (224, 224))

        img = np.float32(original_img) / 255
        blurred_img1 = cv2.GaussianBlur(img, (11, 11), 5)
        blurred_img2 = np.float32(cv2.medianBlur(original_img, 11))/255
        blurred_img_numpy = (blurred_img1 + blurred_img2) / 2

        mask_init = np.ones((28, 28), dtype=np.float32)

        # Convert to torch variables
        img = preprocess_image(img, use_cuda)
        blurred_img = preprocess_image(blurred_img2, use_cuda)
        mask = numpy_to_torch(mask_init, use_cuda)

        if use_cuda:
            upsample = torch.nn.UpsamplingBilinear2d(size=(224, 224)).cuda()
        else:
            upsample = torch.nn.UpsamplingBilinear2d(size=(224, 224))
        optimizer = torch.optim.Adam([mask], lr=learning_rate)

        
        # if not os.path.exists(os.path.join(out_path, f"{model_name}_BBMP.png")):
        model = load_model(model_name, use_cuda)

        target = torch.nn.Softmax()(model(img))
        category = np.argmax(target.cpu().data.numpy())
        # print("Category with highest probability", category)
        # print("Optimizing.. ")

        for i in range(max_iterations):
            upsampled_mask = upsample(mask)
            # The single channel mask is used with an RGB image,
            # so the mask is duplicated to have 3 channel,
            upsampled_mask = \
                upsampled_mask.expand(1, 3, upsampled_mask.size(2),
                                    upsampled_mask.size(3))

            # Use the mask to perturbated the input image.
            perturbated_input = img.mul(upsampled_mask) + \
                blurred_img.mul(1-upsampled_mask)

            noise = np.zeros((224, 224, 3), dtype=np.float32)
            cv2.randn(noise, 0, 0.2)
            noise = numpy_to_torch(noise, use_cuda)
            perturbated_input = perturbated_input + noise

            outputs = torch.nn.Softmax()(model(perturbated_input))
            loss = l1_coeff*torch.mean(torch.abs(1 - mask)) + \
                tv_coeff*tv_norm(mask, tv_beta) + outputs[0, category]

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Optional: clamping seems to give better results
            mask.data.clamp_(0, 1)

        upsampled_mask = upsample(mask)

        save(upsampled_mask, original_img, blurred_img_numpy, model_name, out_path)
