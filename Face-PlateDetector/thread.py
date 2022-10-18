from h11 import Data
import FaceBlur.faceDetector as fd
import PlateBlur.plateDetector as pd
import cv2
import time
from  threading import Thread

class DataManager():
    def __init__(self):
        self.faces = None
        self.plates = None

yoloPath = '/Users/mentxaka/yolov5' 

faceModel = fd.loadYolo(yoloPath)
plateModel = pd.loadYolo(yoloPath)

inPATH = "/Users/mentxaka/Github/TK-VisionArtificial/Face-PlateDetector/Arona_persona.jpg"
outPATH = "/Users/mentxaka/Github/TK-VisionArtificial/Face-PlateDetector/mod_Arona_persona.jpg"

start_time = time.time()

def plateValues(inPATH, plateModel, manager):
    manager.plates = pd.plateDetection(inPATH, plateModel)

def faceValues(inPATH, faceModel, manager):
    manager.faces = fd.faceDetection(inPATH, faceModel)

manager = DataManager()

plateThread = Thread(target=plateValues, args=(inPATH, plateModel, manager))
plateThread.start()
faceThread = Thread(target=faceValues, args=(inPATH, faceModel, manager))
faceThread.start()

plateThread.join()
faceThread.join()

img = pd.plateBoxing(cv2.imread(inPATH),manager.plates)
img = fd.faceBoxing(img,manager.faces)

print("--- %s seconds ---" % (time.time() - start_time))

cv2.imwrite(outPATH,img)
