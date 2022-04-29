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

def NOTWORKINGdetectVideo(path, model):
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
            
            # Start timer
            timer = cv2.getTickCount()

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
            
            # Start timer
            timer = cv2.getTickCount()

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

def internet(path,tracker = cv2.legacy.TrackerBoosting_create()):
    tracker_type = "TLD"
    # Get the video file and read it
    video = cv2.VideoCapture(path)
    ret, frame = video.read()

    frame_height, frame_width = frame.shape[:2]
    # Resize the video for a more convinient view
    frame = cv2.resize(frame, [frame_width//2, frame_height//2])
    # Initialize video writer to save the results
    output = cv2.VideoWriter(f'{tracker_type}.avi', 
                            cv2.VideoWriter_fourcc(*'XVID'), 60.0, 
                            (frame_width//2, frame_height//2), True)
    if not ret:
        print('cannot read the video')
    # Select the bounding box in the first frame
    bbox = cv2.selectROI(frame, False)
    ret = tracker.init(frame, bbox)
    # Start tracking
    while True:
        ret, frame = video.read()
        frame = cv2.resize(frame, [frame_width//2, frame_height//2])
        if not ret:
            print('something went wrong')
            break
        timer = cv2.getTickCount()
        ret, bbox = tracker.update(frame)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        if ret:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else:
            cv2.putText(frame, "Tracking failure detected", (100,80), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
        cv2.putText(frame, tracker_type + " Tracker", (100,20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
        cv2.imshow("Tracking", frame)
        output.write(frame)
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
            
    video.release()
    output.release()
    cv2.destroyAllWindows()

#yoloPath = '/content/yolov5' #path yolo de collab
yoloPath = '/Users/mentxaka/yolov5' #path yolo de Oier
#yoloPath = r"C:\Users\eneko\yolov5" #path yolo de Eneko
modeloYolo = loadYolo(yoloPath)

# path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/PedestrianDetector/images/1stFrame.png"
# detectImage(path ,modeloYolo)

path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/PedestrianDetector/images/SecCameraBoxed.mp4"
internet(path)
# detectVideo(path ,modeloYolo)
