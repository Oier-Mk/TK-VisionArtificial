# -*- coding: utf-8 -*-
"""Eliminar_lineas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P8siZL1PQiNWLcxrgsKjXHbrM_313qcN
"""

def removeHorizontal(image, horizontal = True, vertical = True):
  # Import libraries
  import cv2 as cv
  import numpy as np
  import os

  # Read the original image
  img = cv.imread(image)
  img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  #invertimos el color de la imagen y aplicamos un threshold adaptativo
  img_inv = cv.bitwise_not(img_gray)
  img_thresh = cv.adaptiveThreshold(img_inv, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 15, -2)

  img_thresh_inv = (255- img_thresh)

  if(horizontal):
    # Remove horizontal
    horizontal_kernel = cv.getStructuringElement(cv.MORPH_RECT, (25,1))
    detected_lines = cv.morphologyEx(img_thresh, cv.MORPH_OPEN, horizontal_kernel, iterations=2)
    cnts = cv.findContours(detected_lines, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv.drawContours(img_thresh_inv, [c], -1, (255,255,255), 2)
  if(vertical):
    # Remove vertical
    vertical_kernel = cv.getStructuringElement(cv.MORPH_RECT, (1,25))
    detected_vert_lines = cv.morphologyEx(img_thresh, cv.MORPH_OPEN, vertical_kernel, iterations=2)
    cnts2 = cv.findContours(detected_vert_lines, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts2 = cnts2[0] if len(cnts2) == 2 else cnts2[1]
    for c2 in cnts2:
        cv.drawContours(img_thresh_inv, [c2], -1, (255,255,255), 2)

  #create a new image with the result
  imageFileName = image.split("/")[-1]
  path = image.split("/")
  path.pop(-1)
  nombre = ("mod_"+imageFileName)
  path = '/'.join(path)
  print(os.path.join(path,nombre))
  cv.imwrite(os.path.join(path,nombre),img_thresh_inv)

from google.colab import drive
drive.mount('/content/drive')

removeHorizontal("/content/drive/Shareddrives/Teknei/Limpiador de lineas horizontales/mod_mod_entrenamiento.jpg")