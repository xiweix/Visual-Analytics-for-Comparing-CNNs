import os
import asyncio
import websockets
import base64
import numpy as np
from utils import idxToWord, getSimMatrix, task2ImgGeneration, getRGBhist, task2FullImg, drawContour, getFilteredCamImg
from gradcam_main import gradcamMain
from BBMP import BBMP_process
from smoothgradcam_main import smooth_main
from scorecam_main import scorecamMain
import re
import pickle
import json
from PIL import Image

dataset_path = os.path.join(os.path.dirname(
    os.path.dirname(os.getcwd())), 'dataset')
output_path = os.path.join(os.path.dirname(
    os.path.dirname(os.getcwd())), 'exp_out')
rgb_path = os.path.join(os.path.dirname(
    os.path.dirname(os.getcwd())), 'rgb_out')
os.makedirs(output_path, exist_ok=True)
os.makedirs(rgb_path, exist_ok=True)
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
full_explain_method_list = [
    'Grad-CAM',
    'BBMP',
    'Grad-CAM++',
    'Smooth Grad-CAM++',
    'Score-CAM'
]
explain_name1_list = ['gradcam', 'BBMP', 'gradcampp', 'smoothgradcampp', 'scorecam']
explain_name2_list = ['gradcam_img', 'BBMP_img', 'gradcampp_img', 'smoothgradcampp_img', 'scorecam_img']
explain_name3_list = ['gradcam_mask', 'BBMP_mask', 'gradcampp_mask', 'smoothgradcampp_cam', 'scorecam_mask']
total_imgname = np.load(os.path.join(dataset_path, 'name.npy')).tolist()
total_orglabel = np.load(os.path.join(dataset_path, 'label.npy')).tolist()

async def hello(websocket, path):
    await websocket.send('READY')
    stop = False
    while stop == False:
        rec_m = await websocket.recv()
        if 'Ready' in rec_m:
            rec_list = rec_m.split('***')
            exampleIndex = int(rec_list[1])
            th = float(rec_list[2])
            exampleModel = full_model_list[exampleIndex]
            exampleAcc = ("%.3f" % float(np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'accuracy.npy')).tolist()[1000]))
            example_names = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'example_names.npy')).tolist()
            example_rel = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'example_rel_label.npy')).tolist()
            example_prd = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{exampleModel}', 'example_prd_label.npy')).tolist()
            if exampleModel == 'densenet121':
                idx = [0, 3, 2, 1, 4, 5]
                Z = [x for _,x in sorted(zip(idx,example_names))]
                example_names = Z
            elif exampleModel == 'resnet50':
                idx = [3, 4, 5, 0, 1, 2]
                Z = [x for _,x in sorted(zip(idx,example_names))]
                example_names = Z
            for i in range(len(example_names)):
                img_name = example_names[i]
                base_name = os.path.splitext(img_name)[0]
                output_dir = os.path.join(output_path, base_name)
                sendMsg = 'mainPageExample'
                # org img
                img_path = os.path.join(dataset_path, 'ILSVRC2012_img_val', img_name)
                if os.path.exists(img_path):
                    with open(img_path, 'rb') as imgf:
                        img_data = base64.b64encode(imgf.read()).decode('utf-8')
                else:
                    img_data = '0'
                sendMsg += f'***{img_data}'
                example_rel_content = example_rel[i].split(',')[0]
                sendMsg += f'***{example_rel_content}'
                # sendMsg += f'***{example_acc[i]}'
                example_prd_content = example_prd[i].split(',')[0]
                sendMsg += f'***{example_prd_content}'
                # sendMsg += f'***{example_certainty[i]}'
                # grad cam
                # img_path = os.path.join(output_dir, f'{exampleModel}_{explain_name1_list[0]}.png')
                # if os.path.exists(img_path):
                #     with open(img_path, 'rb') as imgf:
                #         img_data = base64.b64encode(imgf.read()).decode('utf-8')
                # else:
                #     gradcamMain([exampleModel], [img_name], dataset_path, output_path)
                #     if os.path.exists(img_path):
                #         with open(img_path, 'rb') as imgf:
                #             img_data = base64.b64encode(imgf.read()).decode('utf-8')
                #     else:
                #         img_data = '0'
                #         print('gradcam', img_path)
                mask_path = os.path.join(output_dir, f'{exampleModel}_{explain_name3_list[0]}.npy')
                contour_path = os.path.join(output_dir, f'{exampleModel}_{explain_name1_list[0]}_contour.png')
                img_data = drawContour(explain_name1_list[0], mask_path, contour_path, th)
                # mask = np.load(mask_path) / 255.
                # mask = mask.flatten().tolist()
                # mask = json.dumps(mask)
                sendMsg += f'***{img_data}'
                # BBMP
                # img_path = os.path.join(output_dir, f'{exampleModel}_{explain_name1_list[1]}.png')
                # if os.path.exists(img_path):
                #     with open(img_path, 'rb') as imgf:
                #         img_data = base64.b64encode(imgf.read()).decode('utf-8')
                # else:
                #     BBMP_process(dataset_path, img_name, exampleModel, output_path)
                #     if os.path.exists(img_path):
                #         with open(img_path, 'rb') as imgf:
                #             img_data = base64.b64encode(imgf.read()).decode('utf-8')
                #     else:
                #         img_data = '0'
                #         print('BBMP', img_path)
                mask_path = os.path.join(output_dir, f'{exampleModel}_{explain_name3_list[1]}.npy')
                contour_path = os.path.join(output_dir, f'{exampleModel}_{explain_name1_list[1]}_contour.png')
                img_data = drawContour(explain_name1_list[1], mask_path, contour_path, th)
                sendMsg += f'***{img_data}'
                # grad cam++
                # img_path = os.path.join(output_dir, f'{exampleModel}_{explain_name1_list[2]}.png')
                # if os.path.exists(img_path):
                #     with open(img_path, 'rb') as imgf:
                #         img_data = base64.b64encode(imgf.read()).decode('utf-8')
                # else:
                #     gradcamMain([exampleModel], [img_name], dataset_path, output_path)
                #     if os.path.exists(img_path):
                #         with open(img_path, 'rb') as imgf:
                #             img_data = base64.b64encode(imgf.read()).decode('utf-8')
                #     else:
                #         img_data = '0'
                #         print('gradcam++', img_path)
                mask_path = os.path.join(output_dir, f'{exampleModel}_{explain_name3_list[2]}.npy')
                contour_path = os.path.join(output_dir, f'{exampleModel}_{explain_name1_list[2]}_contour.png')
                img_data = drawContour(explain_name1_list[2], mask_path, contour_path, th)
                sendMsg += f'***{img_data}'
                # smooth gradcam++
                # img_path = os.path.join(output_dir, f'{exampleModel}_{explain_name1_list[3]}.png')
                # if os.path.exists(img_path):
                #     with open(img_path, 'rb') as imgf:
                #         img_data = base64.b64encode(imgf.read()).decode('utf-8')
                # else:
                #     smooth_main(dataset_path, [img_name], [exampleModel], output_path)
                #     if os.path.exists(img_path):
                #         with open(img_path, 'rb') as imgf:
                #             img_data = base64.b64encode(imgf.read()).decode('utf-8')
                #     else:
                #         img_data = '0'
                #         print('smoothgradcam++', img_path)
                mask_path = os.path.join(output_dir, f'{exampleModel}_{explain_name3_list[3]}.npy')
                contour_path = os.path.join(output_dir, f'{exampleModel}_{explain_name1_list[3]}_contour.png')
                img_data = drawContour(explain_name1_list[3], mask_path, contour_path, th)
                sendMsg += f'***{img_data}'
                # scorecam
                # img_path = os.path.join(output_dir, f'{exampleModel}_{explain_name1_list[4]}.png')
                # if os.path.exists(img_path):
                #     with open(img_path, 'rb') as imgf:
                #         img_data = base64.b64encode(imgf.read()).decode('utf-8')
                # else:
                #     scorecamMain([exampleModel], [img_name], dataset_path, output_path)
                #     if os.path.exists(img_path):
                #         with open(img_path, 'rb') as imgf:
                #             img_data = base64.b64encode(imgf.read()).decode('utf-8')
                #     else:
                #         img_data = '0'
                #         print('scorecam', img_path)
                mask_path = os.path.join(output_dir, f'{exampleModel}_{explain_name3_list[4]}.npy')
                contour_path = os.path.join(output_dir, f'{exampleModel}_{explain_name1_list[4]}_contour.png')
                img_data = drawContour(explain_name1_list[4], mask_path, contour_path, th)
                sendMsg += f'***{img_data}'
                sendMsg += f'***{th}'
                await websocket.send(sendMsg)
                # org_img = Image.open(img_path)
                # contour_img = Image.open(contour_path)
                # mask_img = Image.open(os.path.join(output_dir, f'{exampleModel}_{explain_name1_list[4]}.png'))
                # mask_on_img = Image.open(os.path.join(output_dir, f'{exampleModel}_{explain_name2_list[4]}.png'))
                # org_img.save(os.path.join('/home/vidi/project/images', f'{base_name}.png'))
                # contour_img.save(os.path.join('/home/vidi/project/images', f'{base_name}_{exampleModel}_contour.png'))
                # mask_img.save(os.path.join('/home/vidi/project/images', f'{base_name}_{exampleModel}_mask.png'))
                # mask_on_img.save.path.join('/home/vidi/project/images', f'{base_name}_{exampleModel}_mask_img.png'))



            print('Finish Main Page')
            await websocket.send(f'FinishMainPageExample***{exampleAcc}')
        
        elif 'requestTask1Img' in rec_m:
            print('requestTask1Img')
            await websocket.send('InitTask1***')
            rec_list = rec_m.split('***')
            task1LabelList = rec_list[1].split(',')
            task1_img_total = []
            for i in range(len(task1LabelList)):
                task1labelIdx = int(task1LabelList[i])
                labelContent = idxToWord(dataset_path, task1labelIdx)
                if task1labelIdx == 124:
                    task1_imgs = task2FullImg(dataset_path, [task1labelIdx])
                else:
                    task1_imgs = np.load(os.path.join(dataset_path, 'ImageNet_Val', 'task1_info', f'label_{task1labelIdx}_task1examplename.npy')).tolist()
                task1_img_total.append(task1_imgs)
                task1Msg = f'task1ImgResult***{i}***{task1labelIdx}.{labelContent}***{len(task1_imgs)}'
                for task1_img in task1_imgs:
                    img_path = os.path.join(dataset_path, 'ILSVRC2012_img_val', task1_img)
                    with open(img_path, 'rb') as fimg:
                        img_data = base64.b64encode(fimg.read()).decode('utf-8')
                    task1Msg += f'***{img_data}***{task1_img}'
                await websocket.send(task1Msg)
            await websocket.send(f'task1ImgDone***')
        
        elif 'requestTask1Exp' in rec_m:
            await websocket.send('InitTask1Exp***')
            rec_list = rec_m.split('***')
            task1currImgName = rec_list[1]
            task1currImgLabel = int(rec_list[2].split('.')[0])
            task1_models = rec_list[3].split(',')
            task1expMethod = rec_list[4]
            compRule = rec_list[5]
            th = 0.0
            task1currImglabelContent = idxToWord(dataset_path, task1currImgLabel).split(',')[0]
            print(task1currImgName)
            base_name = os.path.splitext(task1currImgName)[0]
            output_dir = os.path.join(output_path, base_name)
            imgIndex = total_imgname.index(task1currImgName)
            if task1expMethod == 'Grad-CAM':
                exp_name1 = explain_name1_list[0]
                exp_name2 = explain_name2_list[0]
                exp_name3 = explain_name3_list[0]
            elif task1expMethod == 'BBMP':
                exp_name1 = explain_name1_list[1]
                exp_name2 = explain_name2_list[1]
                exp_name3 = explain_name3_list[1]
            elif task1expMethod == 'Grad-CAM++':
                exp_name1 = explain_name1_list[2]
                exp_name2 = explain_name2_list[2]
                exp_name3 = explain_name3_list[2]
            elif task1expMethod == 'Smooth Grad-CAM++':
                exp_name1 = explain_name1_list[3]
                exp_name2 = explain_name2_list[3]
                exp_name3 = explain_name3_list[3]
            elif task1expMethod == 'Score-CAM':
                exp_name1 = explain_name1_list[4]
                exp_name2 = explain_name2_list[4]
                exp_name3 = explain_name3_list[4]
            for task1Model in task1_models:
                sendTask1Exp = 'task1curTable'
                sendTask1Exp += f'***{task1Model}'
                accuracy = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{task1Model}', 'accuracy.npy')).tolist()
                prd_labels = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{task1Model}', 'predicted.npy')).tolist()
                certainties = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{task1Model}', 'probability.npy')).tolist()
                overall_acc = ("%.3f" % float(accuracy[1000]))
                label_acc = ("%.1f" % float(accuracy[task1labelIdx]))
                sendTask1Exp += f'***{overall_acc}'
                sendTask1Exp += f'***{label_acc}'
                prd_label_content = idxToWord(dataset_path, int(prd_labels[imgIndex]))
                prd_label_content = prd_label_content.split(',')[0]
                certainty = ("%.6f" % float(certainties[imgIndex]))
                sendTask1Exp += f'***{task1currImglabelContent}'
                sendTask1Exp += f'***{prd_label_content}'
                sendTask1Exp += f'***{certainty}'
                # img_path1 = os.path.join(output_dir, f'{task1Model}_{exp_name1}.png')
                # img_path2 = os.path.join(output_dir, f'{task1Model}_{exp_name2}.png')
                # if os.path.exists(img_path1):
                #     with open(img_path1, 'rb') as imgf1:
                #         img_data1 = base64.b64encode(imgf1.read()).decode('utf-8')
                #     with open(img_path2, 'rb') as imgf2:
                #         img_data2 = base64.b64encode(imgf2.read()).decode('utf-8')
                # else:
                #     if task1expMethod == 'Grad-CAM' or task1expMethod == 'Grad-CAM++':
                #         gradcamMain(task1_models, [task1currImgName], dataset_path, output_path)
                #     elif task1expMethod == 'BBMP':
                #         BBMP_process(dataset_path, task1currImgName, task1Model, output_path)
                #     elif task1expMethod == 'Smooth Grad-CAM++':
                #         smooth_main(dataset_path, [task1currImgName], [task1Model], output_path)
                #     elif task1expMethod == 'Score-CAM':
                #         scorecamMain([task1Model], [task1currImgName], dataset_path, output_path)
                #     if os.path.exists(img_path1):
                #         with open(img_path1, 'rb') as imgf1:
                #             img_data1 = base64.b64encode(imgf1.read()).decode('utf-8')
                #         with open(img_path2, 'rb') as imgf2:
                #             img_data2 = base64.b64encode(imgf2.read()).decode('utf-8')
                #     else:
                #         img_data1 = '0'
                #         img_data2 = '0'
                mask_path = os.path.join(output_dir, f'{task1Model}_{exp_name3}.npy')
                mask_img_path = os.path.join(output_dir, f'{task1Model}_{exp_name2}.png')
                contour_path = os.path.join(output_dir, f'{task1Model}_{exp_name1}_contour.png')
                if not os.path.exists(mask_path):
                    if task1expMethod == 'Grad-CAM' or task1expMethod == 'Grad-CAM++':
                        gradcamMain(task1_models, [task1currImgName], dataset_path, output_path)
                    elif task1expMethod == 'BBMP':
                        BBMP_process(dataset_path, task1currImgName, task1Model, output_path)
                    elif task1expMethod == 'Smooth Grad-CAM++':
                        smooth_main(dataset_path, [task1currImgName], [task1Model], output_path)
                    elif task1expMethod == 'Score-CAM':
                        scorecamMain([task1Model], [task1currImgName], dataset_path, output_path)
                img_data1 = drawContour(exp_name1, mask_path, contour_path, th)
                filtered_path = os.path.join(output_dir, f'{task1Model}_{exp_name1}_filtered.png')
                _, img_data2 = getFilteredCamImg(exp_name1, mask_path, mask_img_path, filtered_path, th)
                sendTask1Exp += f'***{img_data1}'
                sendTask1Exp += f'***{img_data2}'
                await websocket.send(sendTask1Exp)
            await websocket.send('task1curTableFinish***')
            cor_path = getSimMatrix(output_dir, task1_models, exp_name1, compRule, dataset_path)
            with open(cor_path, 'rb') as imgf:
                cor_data = base64.b64encode(imgf.read()).decode('utf-8')
            sendTask1Cor = f'task1curSimM***{cor_data}'
            await websocket.send(sendTask1Cor)
            print(f'Finish Task1 Exp of img {task1currImgName}')
        elif 'requestTask1Update' in rec_m:
            rec_list = rec_m.split('***')
            th = float(rec_list[1])
            for task1Model in task1_models:
                sendTask1Exp = 'task1curTable'
                sendTask1Exp += f'***{task1Model}'
                sendTask1Exp += f'***{overall_acc}'
                sendTask1Exp += f'***{label_acc}'
                sendTask1Exp += f'***{task1currImglabelContent}'
                sendTask1Exp += f'***{prd_label_content}'
                sendTask1Exp += f'***{certainty}'
                img_data1 = drawContour(exp_name1, mask_path, contour_path, th)
                _, img_data2 = getFilteredCamImg(exp_name1, mask_path, mask_img_path, filtered_path, th)
                sendTask1Exp += f'***{img_data1}'
                sendTask1Exp += f'***{img_data2}'
                await websocket.send(sendTask1Exp)
            await websocket.send('task1curTableFinish***')
        elif 'runTask2' in rec_m:
            await websocket.send('InitTask2***')
            rec_list = rec_m.split('***')
            task2_model = rec_list[1]
            task2_labels = rec_list[2].split(',')
            task2_exp = rec_list[3]
            th = float(rec_list[4])
            accuracy = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{task2_model}', 'accuracy.npy')).tolist()
            prd_labels = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{task2_model}', 'predicted.npy')).tolist()
            certainties = np.load(os.path.join(dataset_path, 'ImageNet_Val', f'model.{task2_model}', 'probability.npy')).tolist()
            overall_acc = ("%.3f" % float(accuracy[1000]))
            if task2_exp == 'Grad-CAM':
                exp_name1 = explain_name1_list[0]
                exp_name2 = explain_name2_list[0]
                exp_name3 = explain_name3_list[0]
            elif task2_exp == 'BBMP':
                exp_name1 = explain_name1_list[1]
                exp_name2 = explain_name2_list[1]
                exp_name3 = explain_name3_list[1]
            elif task2_exp == 'Grad-CAM++':
                exp_name1 = explain_name1_list[2]
                exp_name2 = explain_name2_list[2]
                exp_name3 = explain_name3_list[2]
            elif task2_exp == 'Smooth Grad-CAM++':
                exp_name1 = explain_name1_list[3]
                exp_name2 = explain_name2_list[3]
                exp_name3 = explain_name3_list[3]
            elif task2_exp == 'Score-CAM':
                exp_name1 = explain_name1_list[4]
                exp_name2 = explain_name2_list[4]
                exp_name3 = explain_name3_list[4]
            task2_imgs = task2ImgGeneration(dataset_path, task2_model, task2_labels)
            if len(task2_imgs) == 10:
                del task2_imgs[3]
                del task2_imgs[5]
            for task2_img in task2_imgs:
                # if task2_img in ['ILSVRC2012_val_00001571.JPEG', 'ILSVRC2012_val_00002597.JPEG', 'ILSVRC2012_val_00034058.JPEG', 'ILSVRC2012_val_00038798.JPEG', 'ILSVRC2012_val_00005918.JPEG']:
                task2SendMsg = 'task2ImgResult'
                base_name = os.path.splitext(task2_img)[0]
                output_dir = os.path.join(output_path, base_name)
                task2ImgIndex = total_imgname.index(task2_img)
                # org img
                img_path = os.path.join(dataset_path, 'ILSVRC2012_img_val', task2_img)
                if os.path.exists(img_path):
                    with open(img_path, 'rb') as imgf:
                        img_data = base64.b64encode(imgf.read()).decode('utf-8')
                else:
                    img_data = '0'
                task2SendMsg += f'***{img_data}'
                # label
                task2ImgLabel = total_orglabel[task2ImgIndex]
                task2ImgLabelAcc = ("%.1f" % float(accuracy[int(task2ImgLabel)]))
                task2ImgLabelContent = idxToWord(dataset_path, int(task2ImgLabel))
                task2ImgLabelContent = task2ImgLabelContent.split(',')[0]
                task2ImgPrdLabelContent = idxToWord(dataset_path, int(prd_labels[task2ImgIndex]))
                task2ImgPrdLabelContent = task2ImgPrdLabelContent.split(',')[0]
                task2ImgCertainty = ("%.6f" % float(certainties[task2ImgIndex]))
                task2SendMsg += f'***{task2ImgLabelContent}'
                task2SendMsg += f'***{task2ImgLabelAcc}'
                task2SendMsg += f'***{task2ImgPrdLabelContent}'
                task2SendMsg += f'***{task2ImgCertainty}'
                print(task2_img, task2ImgPrdLabelContent)
                # img_path1 = os.path.join(output_dir, f'{task2_model}_{exp_name1}.png')
                # img_path2 = os.path.join(output_dir, f'{task2_model}_{exp_name2}.png')
                # if os.path.exists(img_path1):
                #     with open(img_path1, 'rb') as imgf1:
                #         img_data1 = base64.b64encode(imgf1.read()).decode('utf-8')
                #     with open(img_path2, 'rb') as imgf2:
                #         img_data2 = base64.b64encode(imgf2.read()).decode('utf-8')
                # else:
                #     if task2_exp == 'Grad-CAM' or task2_exp == 'Grad-CAM++':
                #         gradcamMain([task2_model], [task2_img], dataset_path, output_path)
                #     elif task2_exp == 'BBMP':
                #         BBMP_process(dataset_path, task2_img, task2_model, output_path)
                #     elif task2_exp == 'Smooth Grad-CAM++':
                #         smooth_main(dataset_path, [task2_img], [task2_model], output_path)
                #     elif task2_exp == 'Score-CAM':
                #         scorecamMain([task2_model], [task2_img], dataset_path, output_path)
                #     if os.path.exists(img_path1):
                #         with open(img_path1, 'rb') as imgf1:
                #             img_data1 = base64.b64encode(imgf1.read()).decode('utf-8')
                #         with open(img_path2, 'rb') as imgf2:
                #             img_data2 = base64.b64encode(imgf2.read()).decode('utf-8')
                #     else:
                #         img_data1 = '0'
                #         img_data2 = '0'
                mask_path = os.path.join(output_dir, f'{task2_model}_{exp_name3}.npy')
                mask_img_path = os.path.join(output_dir, f'{task2_model}_{exp_name2}.png')
                contour_path = os.path.join(output_dir, f'{task2_model}_{exp_name1}_contour.png')
                filtered_path = os.path.join(output_dir, f'{task2_model}_{exp_name1}_filtered.png')
                if not os.path.exists(mask_path):
                    if task2_exp == 'Grad-CAM' or task2_exp == 'Grad-CAM++':
                        gradcamMain([task2_model], [task2_img], dataset_path, output_path)
                    elif task2_exp == 'BBMP':
                        BBMP_process(dataset_path, task2_img, task2_model, output_path)
                    elif task2_exp == 'Smooth Grad-CAM++':
                        smooth_main(dataset_path, [task2_img], [task2_model], output_path)
                    elif task2_exp == 'Score-CAM':
                        scorecamMain([task2_model], [task2_img], dataset_path, output_path)
                img_data1 = drawContour(exp_name1, mask_path, contour_path, th)
                _, img_data2 = getFilteredCamImg(exp_name1, mask_path, mask_img_path, filtered_path, th)
                task2SendMsg += f'***{img_data1}'
                task2SendMsg += f'***{img_data2}'
                # if task2_model == 'resnet152' and task2_exp == 'Smooth Grad-CAM++':
                if task2_model == 'resnet152':
                    rgbHistPath = getRGBhist(dataset_path, task2_img, output_path, rgb_path, task2_model, exp_name3)
                    print('generate hist for: ', task2_img)
                    with open(rgbHistPath, 'rb') as imgf3:
                        img_data3 = base64.b64encode(imgf3.read()).decode('utf-8')
                else:
                    img_data3 = '0'
                task2SendMsg += f'***{img_data3}'
                await websocket.send(task2SendMsg)
            print('finish task2')
            await websocket.send(f'task2ImgDone***{task2_model}***{overall_acc}')

# start_server = websockets.serve(hello, "192.168.1.86", 5050)
start_server = websockets.serve(hello, "169.237.4.185", 5050)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
