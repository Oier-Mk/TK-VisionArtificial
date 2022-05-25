from re import I
import cv2
import numpy as np
import math
import os
import torch
import traceback

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

    #path = r"C:\Users\eneko\GitHub\TK-VisionArtificial\FaceBlur\images\People.jpeg"
    path = "/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/images/People.jpeg"
    
    img, r = selectRange(path)

    xRange1 = int(r[0])
    yRange1 = int(r[1])  
    xRange2 = int(r[2])
    yRange2 = int(r[3])


    pRange1 = (xRange1,yRange1)
    pRange2 = (xRange2,yRange2)

    img = cv2.imread(path)

    results = modelo(img)
    
    i = 0
    while True:
        try:
            print(i)
            x0, y0, x1, y1, _, _ = results.xyxy[0][i].numpy().astype(int)
            x00,y00,x11,y11 = int(x0),int(y0), int(x1), int(y1)
            print(xRange1, yRange1, xRange2, yRange2)
            print(x00,y00,x11,y11)
            #TODO checkear esta condicion, no se porque no se cumple
            izquierdaX = x00>xRange1
            derechaX = x11<xRange2
            arribaY = y00>yRange1
            abajoY = y11<yRange2
            print(izquierdaX, derechaX, arribaY, abajoY)
            if(izquierdaX & derechaX & arribaY & abajoY):
                cv2.rectangle(img, (x00, y00), (x11, y11), (0, 0, 255),-1, 8)
            cv2.rectangle(img, (x00, y00), (x11, y11), (255, 0, 0),-1, 8)
            i+=1
            #print("One face blured")
        except Exception:
            #print(traceback.format_exc())
            print("No more faces detected")
            break
    # Results

    # Display cropped image
    cv2.imshow(path.split(os.path.sep)[-1], img)
    cv2.waitKey(0)

    