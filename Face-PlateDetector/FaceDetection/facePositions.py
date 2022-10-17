import cv2
import numpy as np
import math
import os
import torch
import traceback

relative = os.getcwd()
#yoloPath = os.getcwd() + "\\yolov5"
yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier


def loadYolo(yoloPath):
    weightsPath = relative + os.path.sep + "FaceBlur" + os.path.sep + "weights" + os.path.sep + "best.pt" 
    modeloYolo = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local')  # default
    return modeloYolo

faceModel = loadYolo(yoloPath)

def getFacePosition(path, model):
    img = cv2.imread(path)
    results = model(img)
    positionsArray = []
    while True:       
        try:
            x0, y0, x1, y1, _, _ = results.xyxy[0][i].numpy().astype(int)
            x00,y00,x11,y11 = int(x0),int(y0), int(x1), int(y1)
            positionsArray.append([x00,y00,x11,y11])
            i+=1
        except Exception:
            print(traceback.format_exc())
            print("No more faces detected")
            break
    return positionsArray


print(getFacePosition("/Users/mentxaka/Github/TK-VisionArtificial/Face-PlateDetector/10002.jpg",faceModel))
