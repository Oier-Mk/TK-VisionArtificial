# importing libraries
import cv2
import numpy as np
import torch
import os

def loadYolo(yoloPath):
    relative = os.getcwd() #collab

    print("Cargando yolo")
    weightsPath = relative + os.path.sep + "weights" + os.path.sep + "best.pt" 

    # Model load 
    modeloYolo = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local', force_reload=True)  # default

    print("Yolo cargado")

    return modeloYolo
yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
modeloYolo = loadYolo(yoloPath)


path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/PedestrianDetector/images/SecCamera.mp4"

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(path)

# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")

# Read until video is completed
while(cap.isOpened()):
        
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        
        actualFrame = modeloYolo(frame)

        for index, i in enumerate(actualFrame.xyxy[0]):
            tensor = actualFrame.xyxy[0][index]
            p1 = (int(tensor[0]),int(tensor[1]))
            p2 = (int(tensor[2]),int(tensor[3]))
            print(p1, p2)
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)

        # Display the resulting frame
        cv2.imshow('Frame', frame)
        print("fame")
        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

