import FaceBlur.faceDetector as fd
import PlateBlur.plateDetector as pd
import cv2
import time

yoloPath = '/Users/mentxaka/yolov7' 
#yoloPath = "/content/yolov7"

faceModel = fd.loadYolo(yoloPath)
plateModel = pd.loadYolo(yoloPath)

inPATH = "/Users/mentxaka/Github/TK-VisionArtificial/Face-PlateDetectorV7/Arona_persona.jpg"
outPATH = "/Users/mentxaka/Github/TK-VisionArtificial/Face-PlateDetectorV7/mod_Arona_persona.jpg"

#inPATH = "/content/TK-VisionArtificial/Face-PlateDetectorV7/Arona_persona.jpg"
#outPATH = "/Users/mentxaka/Github/TK-VisionArtificial/Face-PlateDetectorV7/mod_Arona_persona.jpg"

start_time = time.time()*1000

#segundo: matriculas

points = pd.plateDetection(inPATH, plateModel)
img = pd.plateBoxing(cv2.imread(inPATH),points)

#primero: caras

points = fd.faceDetection(inPATH,faceModel)
img = fd.faceBoxing(img,points)

print("Secuential --- %s miliseconds ---" % str((time.time()*1000 - start_time)))

cv2.imwrite(outPATH,img)
