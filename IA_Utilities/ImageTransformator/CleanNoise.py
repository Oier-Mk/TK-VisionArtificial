# Import libraries
import cv2 as cv
import numpy as np
import os

def cleanNoise(origen):

  img_ini = cv.imread(origen)

  img_ini = cv.cvtColor(img_ini, cv.COLOR_BGR2RGB)
  img_ini = cv.cvtColor(img_ini, cv.IMREAD_GRAYSCALE)


  matrix = np.ones(img_ini.shape, dtype = "uint8") * 110 
  img = cv.add(img_ini, matrix)

  dilated_img = cv.dilate(img, np.ones((10), np.uint8)) 


  bg_img = cv.medianBlur(dilated_img, 27)


  diff_img = 255 - cv.absdiff(img, bg_img)


  norm_img = diff_img.copy() # Needed for 3.x compatibility
  cv.normalize(diff_img, norm_img, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)


  _, thr_img = cv.threshold(norm_img, 230, 0, cv.THRESH_TRUNC)
  cv.normalize(thr_img, thr_img, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)


  kernel = np.ones((1),np.uint8)
  img_filtro = cv.dilate(img,kernel,iterations = 1)

  img_gray = cv.cvtColor(img_filtro, cv.COLOR_BGR2GRAY)
  matrix2 = np.ones(img_gray.shape) * 0.8
  img_rgb_higher  = np.uint8(np.clip(cv.multiply(np.float64(img_gray), matrix2),0,255))

  adp = cv.adaptiveThreshold(img_rgb_higher, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 7)

  kernel = np.ones((1,1),np.uint8)
  dilation = cv.dilate(adp,kernel,iterations = 1)
  opening = cv.morphologyEx(dilation, cv.MORPH_OPEN, kernel)

  return opening


