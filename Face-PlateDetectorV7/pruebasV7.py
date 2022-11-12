import argparse
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

'''
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel
'''

# Load model
weights = "/Users/mentxaka/Github/TK-VisionArtificial/Face-PlateDetectorV7/FacePlateBlur/weights/multiclassV7.pt"
yolo = "/Users/mentxaka/yolov7"
model = torch.hub.load(repo_or_dir=yolo, model="custom", path=weights, source='local', force_reload=True)  # defaultattempt_load(weights, map_location=device)  # load FP32 model

'''
import torch
import cv2
import os

#relative = os.getcwd() + os.path.sep + "Face-PlateDetectorV7" + os.path.sep + "PlateBlur" #local
relative = os.getcwd() + os.path.sep + "PlateBlur" #colab


def loadYolo(yoloPath):
    weightsPath = relative + os.path.sep + "weights" + os.path.sep + "platesV7.pt" 
    #weightsPath = "/Users/mentxaka/Github/TK-VisionArtificial/Face-PlateDetector/PlateBlur/weights/best.pt"
    return torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local', force_reload=True)  # default
     
def plateDetection(path,model):
    results = model(path)
    results.print()       
    x0, y0, x1, y1, _, _ =  results.xyxy[0][0].numpy().astype(int) 
    return (int(x0),int(y0)),(int(x1),int(y1))

def plateBoxing(img,points):
    return cv2.rectangle(img, points[0], points[1], (255, 255, 255), -1)
'''