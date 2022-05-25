from re import I
import cv2
import numpy as np
import math
import os
import torch

relative = os.getcwd()

def loadYolo(yoloPath):
    print("Cargando yolo")
    weightsPath = relative + os.path.sep + "weights" + os.path.sep + "best.pt" 

    # Model load 
    modeloYolo = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local')  # default

    print("Yolo cargado")

    return modeloYolo

def selectRange(path):
    # Read image
    img = cv2.imread(path)

    # Select ROI
    return img, cv2.selectROI(img)

def blur(mask, w, h, x1, y1, x2, y2):
    centro = (int(x1+(x2/2)),int(y1+(y2/2)))
    radio = int((math.sqrt(w * w + h * h) // 2)/2)
    cv2.circle(mask, centro, radio, (255, 255, 255), -1)

def getNDetections(results):
    return results.xyxy[0].shape[0]

if __name__ == '__main__' :

    yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
    #yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko

    modelo = loadYolo(yoloPath)

    path = "/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/images/People.jpeg"
    
    #img, r = selectRange(path)

    # xRange1 = int(r[0])
    # yRange1 = int(r[1])  
    # xRange2 = int(r[2])
    # yRange2 = int(r[3])

    # pRange1 = (xRange1,yRange1)
    # pRange2 = (xRange2,yRange2)

    img = cv2.imread(path)

    #TODO tenemos que usar los puntos de arriba para ver la deteccion

    # Inference
    results = modelo(img)
    results.save()

    # Results

    #for i in range(getNDetections(results)):
    for i in range(1):
        x0, y0, x1, y1, _, _ = results.xyxy[0][i].numpy().astype(int)  
        print(x0, y0, x1, y1, _, _ )      
        x00,y00,x11,y11 = int(x0),int(y0), int(x1), int(y1)

        w = x11-x00
        h = y11-y00

        mask = np.zeros(img.shape, dtype='uint8')
        # blur(mask, w, h, x00, y00, x11, y11)
        centro = (int(x00+(x11/2)),int(y00+(y11/2)))
        radio = int((math.sqrt(w * w + h * h) // 2)/2)
        cv2.circle(mask, centro, radio, (255, 255, 255), -1)
        pixelada = np.where(mask > 0, cv2.medianBlur(img, 99), img)


    # Display cropped image
    cv2.imshow(path.split(os.path.sep)[-1], pixelada)
    cv2.waitKey(0)

    