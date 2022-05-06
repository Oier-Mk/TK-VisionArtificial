from counter import getNDetections
import traceback
import cv2
import os
import shutil

def detectImage(path, model):
    #https://docs.ultralytics.com/tutorials/pytorch-hub/
    print("Conteo comenzado")

    try:
        results = model(path)
        results.save()
        nDetections = getNDetections(results)
        nDetections = int(nDetections)
        image = cv2.imread(os.getcwd()+os.path.sep+"runs"+os.path.sep+"detect"+os.path.sep+"exp"+os.path.sep+path.split(os.path.sep)[-1].split('.')[0]+".jpg")
        shutil.rmtree(os.getcwd()+os.path.sep+"runs")
        return(nDetections, image)
    except Exception:
        #print(f"La imagen {path.split(os.path.sep)[-1]} no tiene matriculas reconocobles")
        print(traceback.format_exc())

    print("Conteo completado")