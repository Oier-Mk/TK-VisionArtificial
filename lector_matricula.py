 # coding=utf-8
from Scripts.leer_texto import readText
from Scripts.binarizacion_agresiva import aggressiveBinarization
from Scripts.encuadrar_imagen import encuadraImagen
import os

if __name__ == '__main__':
    path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/Imagenes/coches/cupra.jpg"
    path1 = aggressiveBinarization(path)
    print("path1 ->  " + path1)
    path2 = encuadraImagen(path1)
    print("path2 ->  " + path2)
    print(readText(path2))

