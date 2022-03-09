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

for path in carpetas:
    path = path + os.path.sep + "crops" + os.path.sep + "plate/*"

    imagefiles = glob.glob(path)
    imagefiles.sort() 

    for image in imagefiles:
        print("nombre foto "+image.split("/")[-1])
        for text in readEasy(reader, image):
            print(text[1])
    
    



