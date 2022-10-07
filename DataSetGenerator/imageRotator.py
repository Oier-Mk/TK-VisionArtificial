from cv2 import rotate
import numpy as np
import os
import cv2
from PIL import Image 
import math


def rotatebox(rect, center, degrees):
    rads = math.radians(degrees)

    newpts = []

    for pts in rect:
        diag_x = center[0] - pts[0]
        diag_y = center[1] - pts[1]

        newdx = diag_x * math.cos(rads) - diag_y * math.sin(rads)
        newdy = diag_x * math.sin(rads) + diag_y * math.cos(rads)
        newpts.append( (center[0] + newdx, center[1] + newdy) )

    return newpts

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)

  return result

def annotations2points(path, w, h, angle):

    file = open(path, 'r')
    Lines = file.readlines()
    data = []
    for l in Lines:
        l = l[:-1]
        values = l.split(" ")
        centerX = w * float(values[1])
        centerY = h * float(values[2])
        relW = float(values[3]) * w
        relH = float(values[4]) * h
        puntos = [[centerX-relW,centerY-relH],[centerX+relW,centerY-relH],[centerX+relW,centerY+relH],[centerX-relW,centerY+relH]]
        print(w,h)
        print(values)
        print(centerX)
        print(centerY)
        print(relW)
        print(relH)
        print(puntos)
        print("---------------")
        data.append(rotatebox(puntos,(centerX,centerY),angle))
    return data 

def points2annotations(points):
    pass


def rotator(pathIMG, pathTXT, angle):

    img = cv2.imread(pathIMG) 
    
    img = rotateImage(img, angle)

    h, w, c = img.shape

    annotations = annotations2points(pathTXT, w, h, angle)

    for a in annotations:
        print(a)
        print(a[0])
        print(a[2])
        
        img = cv2.rectangle(img, a[0], a[2], (255, 0, 0), 1)
        
    return img


def main():
    relative = os.getcwd() + os.path.sep + "DataSetGenerator"  + os.path.sep #local
    pathIMG = relative + "media/image (15).jpg"
    pathTXT = relative + "media/image (15) copy.txt"
    rotator(pathIMG,pathTXT,0)


if __name__ == "__main__":
    main()