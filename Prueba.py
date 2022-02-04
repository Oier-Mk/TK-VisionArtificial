from Scripts.eliminar_lineas import removeLines
from Scripts.encuadrar_imagen import encuadraImagen
from Scripts.limpiador_de_imagen import limpiadorImagen

import cv2
import numpy as np
import os

imagen = "/Users/mentxaka/Documents/Trabajo/TK - Vision Artificial/Imagenes/entrenamiento.jpg"
a=imagen
"/".split(a)
print(imagen)
imagen = limpiadorImagen(imagen)
print(imagen)
imagen = encuadraImagen(imagen)
print(imagen)
imagen = removeLines(imagen)
print(imagen)

print("la imagen "+imagen.split("/")[-1]+" se ha transformado")
