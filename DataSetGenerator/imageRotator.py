import cv2
from cv2 import rotate
import numpy as np
import os
from PIL import Image 
import math

def round(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

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

def points2yolo(points,size):

    from cv2 import rotate
    import numpy as np
    import os
    import cv2
    from PIL import Image 
    import math 

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

    #print("0 " + str(propX) + " " + str(propY) + " " + str(propAncho) + " " + str(propAlto))
    #print("0 {:.6f} {:.6f} {:.6f} {:.6f}\n".format(propX, propY, propAncho, propAlto))

    print(width,height)
    print("0 {:.6f} {:.6f} {:.6f} {:.6f}".format(propX, propY, propAncho, propAlto))
    print(puntoX)
    print(puntoY)
    print(ancho)
    print(alto)
    return([(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax)])

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

def annotations2points(path, w, h, angle):
    file = open(path, 'r')
    Lines = file.readlines()
    data = []
    for l in Lines:
        puntos = yolo2points(l,(w,h))
        centerX = puntos[0][0] - puntos[2][0]
        centerY = puntos[0][1] - puntos[2][1]
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
        img = cv2.rectangle(img, a[0], a[2], (255, 0, 0), 1)
        
    return img


def main():
    relative = os.getcwd() + os.path.sep + "DataSetGenerator"  + os.path.sep #local
    pathIMG = relative + "media/image (15).jpg"
    pathTXT = relative + "media/image (15) copy.txt"
    rotator(pathIMG,pathTXT,0)


if __name__ == "__main__":
    main()