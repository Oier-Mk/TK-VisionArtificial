from PedestrianDetector.startYolo import loadYolo
import os

#yoloPath = '/content/yolov5' #path yolo de collab
#yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
#yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko

yoloPath = os.getcwd() + "/yolov5"
pedestrianModel = loadYolo(yoloPath)

    


