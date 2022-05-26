import cv2
import numpy as np
import math
import os
import torch
import argparse

relative = os.getcwd()
yoloPath = os.getcwd() + "/yolov5"

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--imgPath', required=True, type=str, help= 'specify the path of the img you want to blur')
parser.add_argument('-y', '--yoloPath', required= True, type=str, help='specify path of Yolov5 in your device')
args = parser.parse_args()

def loadYolo(yoloPath):
    weightsPath = relative + os.path.sep + "weights" + os.path.sep + "best.pt" 
    modeloYolo = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local')  # default
    return modeloYolo

faceModel = loadYolo(yoloPath)

def selectRange(path):
    img = cv2.imread(path)
    roi = cv2.selectROI(img)
    return img, roi

def blur(mask, w, h, x0, y0, x1, y1):
    centro = (int(x0+((x1-x0)/2)),int(y0+((y1-y0)/2)))
    radio = int((math.sqrt(w * w + h * h) // 2)/1.5)
    cv2.circle(mask, centro, radio, (255, 255, 255), -1)

def getNDetections(results):
    return results.xyxy[0].shape[0]

def faceBlur(path, model, r):

    img = cv2.imread(path)

    xRange1 = int(r[0])
    yRange1 = int(r[1])  
    wRange = int(r[2])
    hRange = int(r[3])
    xRange2 = xRange1 + wRange
    yRange2 = yRange1 + hRange

    results = model(img)
    mask = np.zeros(img.shape, dtype='uint8')
    
    i = 0
    while True:
        try:
            x0, y0, x1, y1, _, _ = results.xyxy[0][i].numpy().astype(int)
            x00,y00,x11,y11 = int(x0),int(y0), int(x1), int(y1)

            izquierdaX = xRange1<x00
            derechaX = x11<xRange2

            arribaY = yRange1<y00
            abajoY = y11<yRange2

            if(izquierdaX & derechaX & arribaY & abajoY):
                blur(mask, x11-x00, y11-y00, x00, y00, x11, y11)
                print("One face blured")

            i+=1
        except Exception:
            print("No more faces detected")
            break
    # Results
    p = np.where(mask > 0, cv2.medianBlur(img, 99), img)
    return i+1,p
