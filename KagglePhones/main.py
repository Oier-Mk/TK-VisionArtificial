# -*- coding: utf-8 -*-

'''
!git clone https://github.com/ultralytics/yolov5
!pip install -r /content/yolov5/requirements.txt
'''
import torch
import cv2
import os
import glob
import traceback
import os.path as Path


def loadYolo(yoloPath):
    print("Cargando yolo")
    weightsPath = relative + os.path.sep + "weights" + os.path.sep + "best.pt" 

    # Model load 
    modeloYolo = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local')  # default

    print("Yolo cargado")

    return modeloYolo

def detectPhone(frame,model):
    result = model(frame)
    x0,y0,x1,y1,_,_ = result.xyxy[0][0].numpy().astype(int)
    return x0,y0,x1,y1

def openCamera(model):
    print("Camera opened")
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        try:
            x0,y0,x1,y1 = detectPhone(frame,model)
            cv2.rectangle(frame,(x0,y0),(x1,y1),(0,255,0),2)
        except:
            #print("No phone detected")
            pass
        cv2.imshow('Phone detector', frame)
        c = cv2.waitKey(1)
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Camera closed")


relative = os.getcwd() #+ os.path.sep + "KagglePhones" #local
print(relative)
#relative = os.getcwd() + os.path.sep + "TK-VisionArtificial" + os.path.sep + "KaggleCoches" #collab

#yoloPath = '/content/yolov5' #path yolo de collab
yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
#yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko
model = loadYolo(yoloPath)

openCamera(model)


