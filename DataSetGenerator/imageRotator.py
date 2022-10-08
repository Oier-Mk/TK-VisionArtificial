import cv2
from cv2 import rotate
import numpy as np
import os
from PIL import Image 
import math

def round(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def rotatePoint(center, point, angle):
    angle = math.radians(angle)

    ox, oy = center
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)

  return result

def points2yolo(points,size):
    width = size[0]
    height = size[1]
    xmin = points[0][0]
    ymin = points[0][1]
    xmax = points[2][0]
    ymax = points[2][1]

    puntoX = abs(xmin-xmax)/2 + xmin
    puntoY = abs(ymin-ymax)/2 + ymin
    ancho = abs(xmin-xmax)
    alto = abs(ymin-ymax)

    propX = puntoX/width
    propY = puntoY/height
    propAncho = ancho/width
    propAlto = alto/height
    return "0 {:.6f} {:.6f} {:.6f} {:.6f}\n".format(propX, propY, propAncho, propAlto)

def yolo2points(values,size):

    values = values[:-1]
    values = values.split(" ")
    values[0] = float(values[0])
    values[1] = float(values[1])
    values[2] = float(values[2])
    values[3] = float(values[3])
    values[4] = float(values[4])

    width = size[0]
    height = size[1]

    propX = values[1]
    propY = values[2]
    propAncho = values[3]
    propAlto = values[4]

    puntoX = width * propX
    puntoY = height * propY
    ancho = width * propAncho
    alto = height * propAlto

    puntos = [(puntoX-ancho/2,puntoY-alto/2),(puntoX+ancho/2,puntoY-alto/2),(puntoX+ancho/2,puntoY+alto/2),(puntoX-ancho/2,puntoY+alto/2)]
    return(puntos)

def annotations2points(path, w, h):
    file = open(path, 'r')
    Lines = file.readlines()
    data = []
    for l in Lines:
        points = yolo2points(l,(w,h))
        data.append(points)
    return data 

def points2annotations(points):
    pass


def rotate(pathIMG, pathTXT, angle):

    img = cv2.imread(pathIMG) 
    
    img = rotateImage(img, angle)

    h, w, c = img.shape

    annotations = annotations2points(pathTXT, w, h)
    
    rotatedAnnotations = []

    for a in annotations:
        points = []
        for p in a:
            points.append(rotatePoint((w/2,h/2),p,angle))
        rotatedAnnotations.append(points)

        #prueba
        print(points[0],points[2])
        img = cv2.rectangle(img, points[0], points[2], (255, 0, 0), 1)
        
    return img


def main():
    relative = os.getcwd() + os.path.sep + "DataSetGenerator"  + os.path.sep #local
    pathIMG = relative + "media/image (15).jpg"
    pathTXT = relative + "media/image (15).txt"
    cv2.imshow('image',cv2.imread(pathIMG))
    cv2.waitKey(0) 
    cv2.imshow('image',rotate(pathIMG,pathTXT,90))
    cv2.waitKey(0) 



if __name__ == "__main__":
    main()