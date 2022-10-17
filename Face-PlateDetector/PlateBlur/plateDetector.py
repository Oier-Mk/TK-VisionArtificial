# -*- coding: utf-8 -*-

'''
!git clone https://github.com/ultralytics/yolov5
!pip install -r /content/yolov5/requirements.txt
'''
import glob
import torch
import cv2
import os
import traceback

relative = os.getcwd() + os.path.sep + "Face-PlateDetector" + os.path.sep + "PlateBlur" #local


def loadYolo(yoloPath):
    weightsPath = relative + os.path.sep + "training" + os.path.sep + "weights" + os.path.sep + "best.pt" 
    return torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local', force_reload=True)  # default
     
def plateDetection(path,model):
    x0, y0, x1, y1, _, _ =  model(path).xyxy[0][0].numpy().astype(int)        
    return (int(x0),int(y0)),(int(x1),int(y1))

def plateBoxing(path,points):
    return cv2.rectangle(cv2.imread(path), points[0], points[1], (255, 0, 0), -1)

def write(path,img):
    cv2.imwrite( path, img)

yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
#yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko


#IMAGENES        
inPATH = "/Users/mentxaka/Github/TK-VisionArtificial/Face-PlateDetector/PlateBlur/media/Arona_2021APX.jpg"
outPATH = "/Users/mentxaka/Github/TK-VisionArtificial/Face-PlateDetector/PlateBlur/results/Arona_2021APX.jpg"

model = loadYolo(yoloPath)
points = plateDetection(inPATH,model)
img = plateBoxing(inPATH,points)
write(outPATH,img)




