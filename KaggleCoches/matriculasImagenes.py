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

#path = "/Users/mentxaka/KaggleCoches/coches/Españoles/*" #path de Oier
path = "KaggleCoches\\coches\\Españoles\\*" #path de Eneko

#yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko

#weightsPath = '/Users/mentxaka/KaggleCoches/weights/best-3.pt' #path de los pesos de Oier
weightsPath = r'C:\Users\eneko\GitHub\TK-VisionArtificial2\KaggleCoches\weights\best-3.pt' #path de los pesos de Eneko

# Model load 
model = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local')  # default
reader = prepareReadEasy()

#folder reading
imagefiles = glob.glob(path)
imagefiles.sort()

print(path)
print(imagefiles)

coordenadas = []
for image in imagefiles:
    
    # Inference
    results = model(image)
    # Results
    print(results.pandas().xyxy[0])
    x0, y0, x1, y1, _, _ = results.xyxy[0][0].numpy().astype(int)
    
    x00,y00,x11,y11 = int(x0),int(y0), int(x1), int(y1)

    print(type(x0))
    cropped_image = image[x00:x11, y00:y11]

    cv2.imwrite("cropped_img.jpg", cropped_image)
    break

    coordenadas.append(coor)
    
#coordenadas de las matriculas de todas las imagenes
print(coordenadas)
#path = "/Users/mentxaka/KaggleCoches/runs/detect/exp*" #path de detecciones de Oier
path = "KaggleCoches\\runs\\detect\\exp*" #path de detecciones de Eneko

#folder reading
print(path)
carpetas = glob.glob(path)
carpetas.sort()

print("CARPETAS")
print(carpetas)
lectura = ""

#dst_path = "/Users/mentxaka/"+"KaggleCoches" + os.path.sep + "results" + os.path.sep #path de Oier
dst_path = "KaggleCoches\\results\\" #path de Eneko

#crear carpeta
if not os.path.isdir(dst_path):
    os.mkdir(dst_path)
    print("Carpeta de salida {} creada".format(dst_path))

for path in carpetas:
    #pathCrops = path + os.path.sep + "crops" + os.path.sep + "plate"+os.path.sep+"*"
    pathCrops = path + "\\crops\\plate\\*" 

    print("path = "+path)
    print("pathCrops = "+pathCrops)


    imagefiles = glob.glob(pathCrops)
    imagefiles.sort() 


    print(imagefiles)


    for image in imagefiles:
        lectura += "nombre foto " + image.split(os.path.sep)[-1] + "\n"
        #lectura de matricula
        for text in readEasy(reader, image):
            lectura += text[1]
        
        lectura += "\n"

        print(lectura)

        #mover carpeta
        shutil.move(image, dst_path)

    try:
        os.remove(path)
    except OSError as e:
        print("Error: %s : %s" % (path, e.strerror))

#pathText = "/Users/mentxaka/"+"KaggleCoches" + os.path.sep + "results" + os.path.sep + "log.txt" #path text de Oier
pathText = r"C:\Users\eneko\GitHub\TK-VisionArtificial2\KaggleCoches" + os.path.sep + "results" + os.path.sep + "log.txt" #path text de Eneko

with open(pathText, 'w') as f:
    f.write(lectura)


    



