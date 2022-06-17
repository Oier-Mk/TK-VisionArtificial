import numpy as np
import cv2 as cv
import os

def rotator(path):

  # Reading and transforming image
  img_read = cv.imread(path)
  grayscale = cv.cvtColor(img_read, cv.COLOR_BGR2GRAY)
  img_thresh_adp = cv.adaptiveThreshold(grayscale, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 7)
  gray = cv.bitwise_not(img_thresh_adp)

  # Calculates the minimum border that contains rotated text
  coords = np.column_stack(np.where(gray > 0))

  # This function gives the rectangle border containing the whole text area, and the rotation angle of this border is the same as that of the text in the figure
  angle = cv.minAreaRect(coords)[-1]

  # Adjust the angle
  if angle < -45:
    angle = -(90+ angle)
  else:
    angle = -angle

  # Affine transformation
  h, w = img_read.shape[:2]
  center = (w//2, h//2)

  # Rotation 
  M = cv.getRotationMatrix2D(center, angle, 1.0)
  rotated = cv.warpAffine(img_read, M, (w, h), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)
  
  return rotated

