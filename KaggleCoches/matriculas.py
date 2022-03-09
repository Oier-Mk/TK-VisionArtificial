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

path = "KaggleCoches/coches/Españoles/*"

# Model
model = torch.hub.load('/Users/mentxaka/yolov5', 'custom', path='KaggleCoches/weights/best-3.pt', source='local')  # default
reader = prepareReadEasy()

#folder reading
imagefiles = glob.glob(path)
imagefiles.sort()

for image in imagefiles:
    
    # Images
    #img = '/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/TratamientoDeImagenes/Imagenes/coches/BMWX1_9689LMN.png'  # or file, Path, PIL, OpenCV, numpy, list

    # Inference
    results = model(image)

    # Results

    data = results.crop(save=True)

path = "runs/detect/exp*"

#folder reading
carpetas = glob.glob(path)
carpetas.sort()

print(carpetas)
lectura = ""

for path in carpetas:
    pathCrops = path + os.path.sep + "crops" + os.path.sep + "plate/*"

    imagefiles = glob.glob(pathCrops)
    imagefiles.sort() 
    
    print(imagefiles)


    for image in imagefiles:
        lectura += "nombre foto " + image.split("/")[-1] + "\n"
        #lectura de matricula
        for text in readEasy(reader, image):
            lectura += text[1]
        
        lectura += "\n"

        print(lectura)

        dst_path = "KaggleCoches" + os.path.sep + "Results" + os.path.sep
        
        #crear carpeta
        if not os.path.isdir(dst_path):
            os.mkdir(dst_path)
            print("Carpeta de salida {} creada".format(dst_path))

        #mover carpeta
        shutil.move(image, dst_path)

    try:
        os.remove(path)
    except OSError as e:
        print("Error: %s : %s" % (path, e.strerror))

with open("KaggleCoches" + os.path.sep + "Results" + os.path.sep + "log.txt", 'w') as f:
    f.write(lectura)


    



