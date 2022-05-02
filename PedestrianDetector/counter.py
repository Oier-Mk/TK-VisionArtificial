import glob
import torch
import cv2
import os
from datetime import datetime
import traceback


relative = os.getcwd() #collab

def createFolders():
    dst_path =  relative + os.path.sep + "results" + os.path.sep
    #crear carpeta
    if not os.path.isdir(dst_path):
        os.mkdir(dst_path)

def loadYolo(yoloPath):
    print("Cargando yolo")
    weightsPath = relative + os.path.sep + "weights" + os.path.sep + "best.pt" 

    # Model load 
    modeloYolo = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local', force_reload=True)  # default

    print("Yolo cargado")

    return modeloYolo

def getNDetections(results):
    return results.xyxy[0].shape[0]

def detectImage(path, model):
    #https://docs.ultralytics.com/tutorials/pytorch-hub/
    print("Conteo comenzado")

    try:
        # Inference
        results = model(path)
        results.save()
        
        print(results.xyxy[0])
        print(results.print())
        print("\033[1mN of objects -> " + str(getNDetections(results)) + '\033[0m')
  
    except Exception:
        #print(f"La imagen {path.split(os.path.sep)[-1]} no tiene matriculas reconocobles")
        print(traceback.format_exc())

    print("Conteo completado")

def detectVideo(path, model):
    #https://docs.ultralytics.com/tutorials/pytorch-hub/
    print("Conteo comenzado")

    try:

        video = cv2.VideoCapture(path)
        
        detections = 0
        lastDetections = 0

        while True:
            ok, frame = video.read()
            if not ok:
                break 

            actualFrame = model(frame)
            actualDetections = getNDetections(actualFrame)
            print(actualDetections)
            if lastDetections < actualDetections:
                detections += abs(actualDetections - lastDetections)
                print("incremento " + str(abs(actualDetections - lastDetections)) + ", total " + str(detections))
            
            lastDetections = actualDetections
        
        print(detections)
        
    except Exception:
        #print(f"La imagen {path.split(os.path.sep)[-1]} no tiene matriculas reconocobles")
        print(traceback.format_exc())

    print("Conteo completado")


#yoloPath = '/content/yolov5' #path yolo de collab
yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
#yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko
modeloYolo = loadYolo(yoloPath)
#modeloYolo = None

# path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/PedestrianDetector/images/1stFrame.png"
# detectImage(path ,modeloYolo)

path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/PedestrianDetector/images/rainyDay.mp4"
path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/PedestrianDetector/images/SecCamera.mp4"
#internet(path)
detectVideo(path, modeloYolo)
# detectVideo(path ,modeloYolo)
