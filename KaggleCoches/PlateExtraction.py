# -*- coding: utf-8 -*-

'''
!git clone https://github.com/ultralytics/yolov5
!pip install -r /content/yolov5/requirements.txt
'''
import glob
import torch
import cv2
import os
from datetime import datetime
import traceback

#relative = os.getcwd() + os.path.sep + "TK-VisionArtificial" + os.path.sep + "KaggleCoches" #local
relative = os.getcwd() #collab


def loadYolo(yoloPath):
    print("Cargando yolo")
    weightsPath = relative + os.path.sep + "weights" + os.path.sep + "best.pt" 

    # Model load 
    modeloYolo = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local', force_reload=True)  # default

    print("Yolo cargado")

    return modeloYolo

def createFolders():
    dst_path =  relative + os.path.sep + "results" + os.path.sep
    #crear carpeta
    if not os.path.isdir(dst_path):
        os.mkdir(dst_path)
        os.mkdir(dst_path+os.path.sep+"frames")
        os.mkdir(dst_path+os.path.sep+"crops")


def video2Frames(path):
    print("Lectura del video comenzada")

    pathVideoFrames = relative + os.path.sep + "results" + os.path.sep + "frames" + os.path.sep 
    
    cap = cv2.VideoCapture(path)
    # # Read until video is completed
    cont = 0
    while(cap.isOpened()):
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            if cont % 10 == 0:
                now = datetime.now()
                path = pathVideoFrames + str(now) +".jpeg"
                if not cv2.imwrite(path, frame):
                    print(traceback.format_exc())
                else:
                    print(f"Se ha extraido un frame de la imagen {now}" )
        else: 
            break
        cont = cont+1


    print("Lectura del video completada")
        

def plateCrop(path, model):
    print("Lectura de carpeta comenzada")

    #folder reading
    imagefiles = glob.glob(path)
    imagefiles.sort()


    coordenadas = []
    for image in imagefiles:
        try:
            # Inference
            results = model(image)
            # Results
            x0, y0, x1, y1, _, _ = results.xyxy[0][0].numpy().astype(int)        
            x00,y00,x11,y11 = int(x0),int(y0), int(x1), int(y1)
            imageOCV = cv2.imread(image)
            cropped_image = imageOCV[y00:y11, x00:x11] 
            cv2.imwrite(relative + os.path.sep + "results" + os.path.sep + "crops" + os.path.sep + image.split(os.path.sep)[-1], cropped_image)
         
        except Exception:
            print(f"La imagen {image.split(os.path.sep)[-1]} no tiene matriculas reconocobles")
            #print(traceback.format_exc())

    print("Lectura de carpeta completada")


#yoloPath = '/content/yolov5' #path yolo de collab
yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
#yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko
modeloYolo = loadYolo(yoloPath)

createFolders()

# #IMAGENES        
#path = relative + os.path.sep + "coches" + os.path.sep + "Españoles" + os.path.sep + "*" 

#VIDEO
path = relative + os.path.sep + "coches" + os.path.sep + "parkingUD.MOV"
video2Frames(path)

path = relative + os.path.sep + "results" + os.path.sep + "frames" + os.path.sep + "*"
plateCrop(path, modeloYolo)


