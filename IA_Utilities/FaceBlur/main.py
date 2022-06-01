import cv2
import numpy as np
import math
import os
import torch
import traceback

relative = os.getcwd()
yoloPath = os.getcwd() + "/yolov5"

def loadYolo(yoloPath):
    weightsPath = relative + os.path.sep + "FaceBlur" + os.path.sep + "weights" + os.path.sep + "best.pt" 
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

    print(r)
    for h in range(len(r)):
        cv2.circle(img, (r[h][0],r[h][1]), radius=5, color=(0, 0, 255), thickness=-1)
    results = model(img)
    mask = np.zeros(img.shape, dtype='uint8')
    
    i = 0
    p = (0,0)
    while True:       
        try:
            x0, y0, x1, y1, _, _ = results.xyxy[0][i].numpy().astype(int)
            x00,y00,x11,y11 = int(x0),int(y0), int(x1), int(y1)
            cv2.rectangle(img, (x00,y00),(x11,y11),color=(0, 0, 255), thickness=2)
            for a in range(len(r)):
                print("**PUNTO DE ARRAY**")
                p = r[a]
                print(p)
                print(x00, y00, x11, y11)
                ejeX = x00<p[0] & p[0]<x11
                ejeY = y00<p[1] & p[1]<y11
                print(ejeX,ejeY)
                if(ejeX & ejeY):
                    blur(mask, x11-x00, y11-y00, x00, y00, x11, y11)
                    print("One face blured")
                    break
            print("--CARA DE YOLO--")
            i+=1
        except Exception:
            print(traceback.format_exc())
            print("No more faces detected")
            break
    # Results
    p = np.where(mask > 0, cv2.medianBlur(img, 99), img)
    # cv2.imshow("foto",p)
    # cv2.waitKey(0)
    return i+1,p
