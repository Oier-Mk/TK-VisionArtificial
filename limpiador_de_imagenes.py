# -*- coding: utf-8 -*-
"""Limpiador_de_imagenes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rUD4csOqHt9ZaJcjZVpvHKrEuJiSPo46
"""

def limpiadorImagenes(origen,destino):
  # Import libraries
  import cv2 as cv
  import numpy as np
  import glob
  import os

  #almacenamos las imagenes de input en una variable y las ordenamos 
  imagefiles = glob.glob(origen)
  imagefiles.sort()

  #comprobamos si la carpeta de destino ya existe o hay que crearla
  if os.path.isdir(destino):
    print("Carpeta de salida {} ya existe".format(destino))
  else:
    os.mkdir(destino)
    print("Carpeta de salida {} creada".format(destino))

  #recorremos la lista de imagenes 
  for filename in imagefiles:
    #leemos y ajustamos la imagen
    img_ini = cv.imread(filename)
    img_ini = cv.cvtColor(img_ini, cv.COLOR_BGR2RGB)
    img_ini = cv.cvtColor(img_ini, cv.IMREAD_GRAYSCALE)

    #aumentamos el brillo de la imagen
    matrix = np.ones(img_ini.shape, dtype = "uint8") * 110 
    img = cv.add(img_ini, matrix)

    #dilatar las letras 
    dilated_img = cv.dilate(img, np.ones((10), np.uint8)) 

    #obtenemos el fonde de la imagen 
    bg_img = cv.medianBlur(dilated_img, 27)

    #calculamos la diferencia entre la imagen original y el fondo, de manera que el fondo queda casi eliminado
    diff_img = 255 - cv.absdiff(img, bg_img)

    #normalizamos la imagen 
    norm_img = diff_img.copy() # Needed for 3.x compatibility
    cv.normalize(diff_img, norm_img, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)
    
    #aplicamos un threshold y volvemos a normalizar
    _, thr_img = cv.threshold(norm_img, 230, 0, cv.THRESH_TRUNC)
    cv.normalize(thr_img, thr_img, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)

    #dilatamos las letras para poder apreciarlas mejor 
    kernel = np.ones((1),np.uint8)
    img_filtro = cv.dilate(img,kernel,iterations = 1)

    img_gray = cv.cvtColor(img_filtro, cv.COLOR_BGR2GRAY)

    #bajamos el contraste de la imagen y aplicamos 'clip' para solucionar posibles errores
    matrix2 = np.ones(img_gray.shape) * 0.8
    img_rgb_higher  = np.uint8(np.clip(cv.multiply(np.float64(img_gray), matrix2),0,255))

    #aplicamos un threshold adaptativo
    adp = cv.adaptiveThreshold(img_rgb_higher, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 7)

    #aplicamos algunas transformaciones morfologicas --> dilatacion y opening (quitar puntos alrededor de las letras)
    kernel = np.ones((1,1),np.uint8)
    dilation = cv.dilate(adp,kernel,iterations = 1)
    opening = cv.morphologyEx(dilation, cv.MORPH_OPEN, kernel)

    #nos quedamos con el nombre de la imagen y la almacenamos en la carpeta 
    imageFileName = filename.split("/")[-1]
    cv.imwrite(os.path.join(destino,imageFileName),opening)

  print("Proceso finalizado")

limpiadorImagenes("/content/drive/Shareddrives/Teknei/Limpieza automatizada/Input/*","/content/drive/Shareddrives/Teknei/Limpieza automatizada/Output")