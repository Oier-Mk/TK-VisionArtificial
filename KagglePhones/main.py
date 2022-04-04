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

relative = os.getcwd() #local
#relative = os.getcwd() + os.path.sep + "TK-VisionArtificial" + os.path.sep + "KaggleCoches" #collab


def loadYolo(yoloPath):
    print("Cargando yolo")
    weightsPath = relative + os.path.sep + "weights" + os.path.sep + "best.pt" 

    # Model load 
    modeloYolo = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local')  # default

    print("Yolo cargado")

    return modeloYolo

def openCamera():
    print("Camera opened")
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.75, fy=0.75, interpolation=cv2.INTER_AREA)
        
        cv2.imshow('Phone detector', frame)
        c = cv2.waitKey(1)
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Camera closed")


#yoloPath = '/content/yolov5' #path yolo de collab
yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
#yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko
modeloYolo = loadYolo(yoloPath)

openCamera()


