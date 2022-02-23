

def maximizeImage(input):
  import numpy as np
  import cv2 as cv
  import os
  import pytesseract
  import os

  img_read = cv.imread(input, cv.IMREAD_GRAYSCALE)

  image = cv.resize(img_read,(int(img_read.shape[1]*1.5),int(img_read.shape[0]*1.5)))

  #create a new image with the result
  imageFileName = input.split("/")[-1]
  path = input.split("/")
  path.pop(-1)
  nombre = ("resized_"+imageFileName)
  path = '/'.join(path)
  path = os.path.join(path,nombre)
  cv.imwrite(path,image)
  print("Imagen redimensionada")
  return path

