from leer_texto import prepareReadEasy, readEasy
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

reader = prepareReadEasy()

path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/KaggleCoches/results/crops/*"

print(textReading(path,reader))

print(True)