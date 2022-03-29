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
from datetime import datetime
import re
import traceback




def loadModel(yoloPath):

    print("frames comenzados")
    #weightsPath = os.path.sep + "content" + os.path.sep + "TK-VisionArtificial" + os.path.sep + "KaggleCoches"+os.path.sep+"weights"+os.path.sep+"best-3.pt" 
    weightsPath = os.getcwd() + os.path.sep + "weights"+os.path.sep+"best-3.pt" 
    #weightsPath = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/KaggleCoches/weights/best-3.pt"
    # Model load 
    model = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local')  # default
    reader = prepareReadEasy()

    #dst_path =  os.path.sep + "content" + os.path.sep + "TK-VisionArtificial" + os.path.sep + "KaggleCoches" + os.path.sep + "results" + os.path.sep
    dst_path =  os.getcwd() + os.path.sep + "results" + os.path.sep

    #crear carpeta
    if not os.path.isdir(dst_path):
        os.mkdir(dst_path)
        os.mkdir(dst_path+os.path.sep+"frames")
        os.mkdir(dst_path+os.path.sep+"crops")

    print("frames finalizados")

    return model, reader

def video2Frames(path):
    print("Lectura del video comenzada")

    #pathVideoFrames = os.path.sep + "content" + os.path.sep + "TK-VisionArtificial" + os.path.sep + "KaggleCoches"+os.path.sep+"results"+os.path.sep+"frames"+os.path.sep 
    pathVideoFrames = os.getcwd() + os.path.sep+"results" + os.path.sep + "frames" + os.path.sep 
    
    cap = cv2.VideoCapture(path)
    # # Read until video is completed
    cont = 0
    while(cap.isOpened()):
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            if cont % 10 == 0:
                now = datetime.now()
                path = pathVideoFrames+str(now)+".jpeg"
                cv2.imwrite(path, frame)
                print(f"imagen {now} ha sido recortada" )
        else: 
            break
        cont = cont+1


    print("Lectura del video completada")
        

def folderReading(path, model):
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

            #cv2.imwrite(os.path.sep + "content" + os.path.sep + "TK-VisionArtificial" + os.path.sep + "KaggleCoches"+os.path.sep+"results"+os.path.sep+"crops"+os.path.sep+image.split(os.path.sep)[-1], cropped_image)
            cv2.imwrite(os.getcwd() + os.path.sep + "results" + os.path.sep + "crops" + os.path.sep + image.split(os.path.sep)[-1], cropped_image)
         
        except Exception:
          print(traceback.format_exc())

    print("Lectura de carpeta completada")

def getRepIndexes(array, element):
    indexes = [] 
    if element not in array: return None
    for idx, ele in enumerate(array):
        if (element == ele): indexes.append(idx)
    return indexes

def remSpace(lecturaResultado):
    print("borrando espacio")
    prov = []
    for idx, plate in enumerate(lecturaResultado):
        prov.append(plate.replace(" ",""))
    lecturaResultado = prov
    print("espacios borrados")
    return(lecturaResultado)


def remEquals(lecturaNombre, lecturaResultado):
    print("borrando iguales")
    for plate in lecturaResultado:
        indexes = getRepIndexes(lecturaResultado, plate)
        indexes.pop(0)
        for i,idx in enumerate(indexes):
            lecturaResultado.pop(idx-i)
            lecturaNombre.pop(idx-i)
    print("iguales borrados")
    return(lecturaNombre,lecturaResultado)
        

def deleteIncorrectPlates(lecturaNombre,lecturaResultado):    
    provNombre = []
    provResultado = []
    for idx, val in enumerate(lecturaResultado):
        match = re.search('([1234567890]{4})([BCDFGHJKLMNPQRSTWXYZ]{3})', val) 
        if match:
            print(f"YES! We have a match! idx = {idx} $$ val = {lecturaResultado[idx]}")
            provNombre.append(lecturaNombre[idx])
            provResultado.append(lecturaResultado[idx])

    print(provResultado)
    return(provNombre,provResultado)

def textReading(path,reader):   
    print("Lectura del OCR comenzada")

    #folder reading
    results = glob.glob(path)
    results.sort()
    lecturaNombre = []
    lecturaResultado = []
    for image in results:
        try:
            #lectura de matricula
            lecturaNombre.append(image.split(os.path.sep)[-1])
            prov = ""
            for text in readEasy(reader, image):
                prov+=text[1]
            lecturaResultado.append(prov)
            print("la imagen "+image.split(os.path.sep)[-1]+" SI tiene matrículas legibless")
        except Exception:
            print(traceback.format_exc())
            print("la imagen "+image.split(os.path.sep)[-1]+" no tiene matrículas legibless")
    print("Lectura del OCR completada")

    return(lecturaNombre,lecturaResultado)

def regExp(lecturaNombre,lecturaResultado): 

    lecturaResultado = remSpace(lecturaResultado)

    lecturaNombre,lecturaResultado = deleteIncorrectPlates(lecturaNombre,lecturaResultado)
    
    lecturaNombre,lecturaResultado = remEquals(lecturaNombre,lecturaResultado)

    prov = "" 
    for i, name in enumerate(lecturaNombre): 
        prov += (name +"\t"+lecturaResultado[i] +"\n")
    
    #pathText = os.path.sep + "content" + os.path.sep + "TK-VisionArtificial" + os.path.sep + "KaggleCoches" + os.path.sep + "results" + os.path.sep + "log.txt" 
    pathText = os.getcwd() + os.path.sep + "results" + os.path.sep + "log.txt" 
    with open(pathText, 'w') as f:
        f.write(prov)

    print("txt generado")


#yoloPath = '/content/yolov5'
yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
#yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko
model, reader = loadModel(yoloPath)

# #IMAGENES        
#path = os.getcwd()+os.path.sep+"coches"+os.path.sep+"Españoles"+os.path.sep+"*" 

#VIDEO
# path = os.getcwd() + os.path.sep + "coches" + os.path.sep + "parkingUD.MOV"
# video2Frames(path)
# path = os.getcwd() + os.path.sep + "results" + os.path.sep + "frames" + os.path.sep + "*"

# folderReading(path, model)
path = os.getcwd() + os.path.sep + os.path.sep + "results" + os.path.sep + "crops" + os.path.sep + "*" 
lecturaNombres, lectureResultados = textReading(path,reader)
regExp(lecturaNombres, lectureResultados)
