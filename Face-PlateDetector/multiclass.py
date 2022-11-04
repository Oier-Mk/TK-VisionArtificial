import FacePlateBlur.facePlateDetector as fpd
import cv2
import time

yoloPath = '/Users/mentxaka/yolov5'

multiclassModel = fpd.loadYolo(yoloPath)

inPATH = "/Users/mentxaka/Github/TK-VisionArtificial/Face-PlateDetector/Arona_persona.jpg"
outPATH = "/Users/mentxaka/Github/TK-VisionArtificial/Face-PlateDetector/mod_Arona_persona.jpg"

start_time = time.time()

points = fpd.multiclassDetection(inPATH,multiclassModel)
img = fpd.multiclassBoxing(cv2.imread(inPATH),points)

print("Multiclass --- %s seconds ---" % (time.time() - start_time))

cv2.imwrite(outPATH,img)
