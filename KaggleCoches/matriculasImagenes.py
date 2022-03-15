# -*- coding: utf-8 -*-

'''
!git clone https://github.com/ultralytics/yolov5
!pip install -r /content/yolov5/requirements.txt
'''
import torch
import numpy
import cv2
import pandas as pd
import os
import glob
from leer_texto import prepareReadEasy, readEasy
import shutil

def loadModel(yoloPath):

    weightsPath = "KaggleCoches"+os.path.sep+"weights"+os.path.sep+"best-3.pt" #path de los pesos de Oier

    # Model load 
    model = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local')  # default
    reader = prepareReadEasy()

    dst_path = "KaggleCoches" + os.path.sep + "results" + os.path.sep #path de Oier

    #crear carpeta
    if not os.path.isdir(dst_path):
        os.mkdir(dst_path)
        os.mkdir(dst_path+os.path.sep+"frames")
        os.mkdir(dst_path+os.path.sep+"crops")

    
    return model, reader

def video2Frames(path):
    print("Lectura del video comenzadad")

    pathVideoFrames = "KaggleCoches"+os.path.sep+"results"+os.path.sep+"frames"+os.path.sep 
    cap = cv2.VideoCapture(path)
    # # Read until video is completed
    cont = 0
    while(cap.isOpened()):
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            if cont % 5 == 0:
                cv2.imwrite(pathVideoFrames+str(cont)+".jpeg", frame)
        else: 
            break
        cont = cont+1


    print("Lectura del video completada")
        

def folderReading(path, model):
    print("Lectura de carpeta comenzadad")

    #folder reading
    imagefiles = glob.glob(path)
    imagefiles.sort()


    coordenadas = []
    for image in imagefiles:
        print(image)
        try:
            # Inference
            results = model(image)
            # Results
            x0, y0, x1, y1, _, _ = results.xyxy[0][0].numpy().astype(int)        
            x00,y00,x11,y11 = int(x0),int(y0), int(x1), int(y1)
            imageOCV = cv2.imread(image)
            cropped_image = imageOCV[y00:y11, x00:x11] 
            cv2.imwrite("KaggleCoches"+os.path.sep+"results"+os.path.sep+"crops"+os.path.sep+image.split(os.path.sep)[-1], cropped_image)
        
        except:
            print("la imagen "+image.split(os.path.sep)[-1]+" no tiene matrículas reconocibles")
        
    print("Lectura de carpeta completada")


def textReading(path,reader):   
    print("Lectura del OCR comenzadad")

    #folder reading
    results = glob.glob(path)
    results.sort()
    lectura = ""

    for image in results:
        try:
            lectura += "nombre foto " + image.split(os.path.sep)[-1] + "\n"
            #lectura de matricula
            for text in readEasy(reader, image):
                lectura += text[1]
            
            lectura += "\n"
            pathText = "KaggleCoches" + os.path.sep + "results" + os.path.sep + "log.txt" #path text de Oier
        except:
            print("la imagen "+image.split(os.path.sep)[-1]+" no tiene matrículas legibless")
    print("Lectura del OCR completada")

    with open(pathText, 'w') as f:
        f.write(lectura)


yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
#yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko
model, reader = loadModel(yoloPath)

# #IMAGENES        
# path = "KaggleCoches"+os.path.sep+"coches"+os.path.sep+"Españoles"+os.path.sep+"*" 
# path = "KaggleCoches"+os.path.sep+"coches"+os.path.sep+"Españoles"+os.path.sep+"*"

# #VIDEO
# path = "KaggleCoches"+os.path.sep+"coches"+os.path.sep+"video.MOV" 
# video2Frames(path)
#path = "KaggleCoches"+os.path.sep+"results"+os.path.sep+"frames"+os.path.sep+"*"

#folderReading(path, model)
path = "KaggleCoches"+os.path.sep+"results"+os.path.sep+"crops"+os.path.sep+"*" 
textReading(path,reader)
