from image import detectImage
from video import detectVideo
from startYolo import loadYolo


#yoloPath = '/content/yolov5' #path yolo de collab
yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
#yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko
modeloYolo = loadYolo(yoloPath)

#TODO 
#insertar imagen desde consola o web

#path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/PedestrianDetector/images/SecCamera.png"

#detectVideo(path, modeloYolo)
# nDetections, image = detectImage(path, modeloYolo)
# print("\033[1mN of objects -> " + str(nDetections) + '\033[0m')
# import cv2
# cv2.imshow('',image)
# cv2.waitKey(0) 


#https://fastapi.tiangolo.com/tutorial/request-files/#file-parameters-with-uploadfile


