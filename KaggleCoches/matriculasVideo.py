# -*- coding: utf-8 -*-

'''
!git clone https://github.com/ultralytics/yolov5
!pip install -r /content/yolov5/requirements.txt
'''

import torch
import pandas as pd
import os
import glob
from leer_texto import prepareReadEasy, readEasy
import shutil
import cv2

# path = "/Users/mentxaka/KaggleCoches/coches/video.MOV" #path de Oier
# path = r"C:\Users\eneko\GitHub\TK-VisionArtificial2\KaggleCoches\coches\video.MOV" #path de Eneko

#pathVideoFrames = "/Users/mentxaka/KaggleCoches/coches/videoFrames/" #path de Oier
#pathVideoFrames = r"C:\Users\eneko\GitHub\TK-VisionArtificial2\KaggleCoches\coches\videoFrames\" #path de Eneko
# cap = cv2.VideoCapture(path)
# # Read until video is completed
# cont = 0
# while(cap.isOpened()):
#   # Capture frame-by-frame
#     ret, frame = cap.read()
#     if  ret == True:
#         if cont % 5 == 0:
#             cv2.imwrite(pathVideoFrames+str(cont)+".jpeg",frame)
#             print(cont%5)
 
#         cont = cont+1
#         print(cont)
#     else:
#         break


# print("fin deteccion frames") 

# path = "/Users/mentxaka/KaggleCoches/coches/videoFrames/*" #path de Oier
# path = r"C:\Users\eneko\GitHub\TK-VisionArtificial2\KaggleCoches\coches\videoFrames\*" #path de Eneko

#yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko

#weightsPath = '/Users/mentxaka/KaggleCoches/weights/best-3.pt' #path de los pesos de Oier
weightsPath = r'C:\Users\eneko\GitHub\TK-VisionArtificial2\KaggleCoches\weights\best-3.pt' #path de los pesos de Eneko

# Model
model = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local')  # default
reader = prepareReadEasy()

# #folder reading
# imagefiles = glob.glob(path)
# imagefiles.sort()

# print(imagefiles)


# for image in imagefiles:
    
#     # Inference
#     results = model(image)

#     # Results

#     data = results.crop(save=True)

#path = "/Users/mentxaka/KaggleCoches/runs/detect/exp*" #path de detecciones de Oier
path = r"C:\Users\eneko\GitHub\TK-VisionArtificial2\KaggleCoches\runs\detect\exp*" #path de detecciones de Eneko

#folder reading
carpetas = glob.glob(path)
carpetas.sort()

print(carpetas)
lectura = ""

#dst_path = "/Users/mentxaka/"+"KaggleCoches" + os.path.sep + "results" + os.path.sep #path de Oier
dst_path = r"C:\Users\eneko\GitHub\TK-VisionArtificial2\KaggleCoches" + os.path.sep + "results" + os.path.sep #path de Eneko
#crear carpeta
if not os.path.isdir(dst_path):
    os.mkdir(dst_path)
    print("Carpeta de salida {} creada".format(dst_path))

for path in carpetas:
    pathCrops = path + os.path.sep + "crops" + os.path.sep + "plate"+os.path.sep+"*"

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
pathText = "C:\Users\eneko\GitHub\TK-VisionArtificial2\KaggleCoches" + os.path.sep + "results" + os.path.sep + "log.txt" #path text de Eneko

with open(pathText, 'w') as f:
    f.write(lectura)


    



