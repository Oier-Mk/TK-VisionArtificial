import torch
import os

relative = os.getcwd() #collab

def loadYolo(yoloPath):
    print("Cargando yolo")
    weightsPath = relative + os.path.sep + "weights" + os.path.sep + "best.pt" 
    # Model load 
    modeloYolo = torch.hub.load(yoloPath, 'custom', path=weightsPath, source='local', force_reload=True)  # default
    print("Yolo cargado")

    return modeloYolo