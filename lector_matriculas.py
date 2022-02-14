from Scripts.leer_texto import readText
from Scripts.binarizacion_agresiva import aggressiveBinarization
from Scripts.encuadrar_imagen import encuadraImagen
import cv2
import os

if __name__ == '__main__':
    
    path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/Imagenes/coches/"

    listadeimagenes = os.listdir(path)

    print(listadeimagenes)

    for i in listadeimagenes:
    	aggressiveBinarization(path+i)

    path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/Imagenes/coches/mascara/"

    listadeimagenes = os.listdir(path)

    print(listadeimagenes)

    for i in listadeimagenes:
    	encuadraImagen(path+i)
    
    path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/Imagenes/coches/encuadrada/"
    
    listadeimagenes = os.listdir(path)


    for i in listadeimagenes:
   		print(readText(path+i))

