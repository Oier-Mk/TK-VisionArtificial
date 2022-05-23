import cv2
import numpy as np
import math
import os

if __name__ == '__main__' :

    # Read image
    path = "/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/images/People.jpeg"
    img = cv2.imread(path)

    # Select ROI
    r = cv2.selectROI(img)

    x1 = int(r[0])
    y1 = int(r[1])  
    x2 = int(r[2])
    y2 = int(r[3])

    p1 = (x1,y1)
    p2 = (x2,y2)

    w = x2-x1
    h = y2-y1

    centro = (int(x1+(x2/2)),int(y1+(y2/2)))
    radio = int((math.sqrt(w * w + h * h) // 2)/2)

    mascara = np.zeros(img.shape, dtype='uint8')
    cv2.circle(mascara, centro, radio, (255, 255, 255), -1)

    pixelada = np.where(mascara > 0, cv2.medianBlur(img, 99), img)

    # Display cropped image
    cv2.imshow(path.split(os.path.sep)[-1], pixelada)
    cv2.waitKey(0)