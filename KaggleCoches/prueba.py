from leer_texto import prepareReadEasy, readEasy
import os
import glob
import torch
import traceback

from matriculas import loadModel


yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier

model, reader = loadModel(yoloPath)

path = os.getcwd() + os.path.sep + "results" + os.path.sep + "crops" + os.path.sep + "*" 

print(textReading(path,reader))

print(True)