from Scripts.eliminar_lineas import removeLines
from Scripts.encuadrar_imagen import encuadraImagen
from Scripts.limpiador_de_imagen import limpiadorImagen
from Scripts.rotacion_imagen import alignImage
from Scripts.tesseract import readText
from Scripts.cambiar_tamanyo import maximizeImage

import cv2
import numpy as np
import os

def getText(input):
	try:
		print(input)
		imagen = limpiadorImagen(input)
		print(imagen)
		imagen = encuadraImagen(imagen)
		print(imagen)
		imagen = maximizeImage(imagen)
		print(imagen)
		texto = readText(imagen)
		print(texto)
		print("la imagen "+input.split("/")[-1]+" se ha transformado")
	except:
		print("Ha  habido algun error en el proceso")

input1 = "/Users/mentxaka/Documents/Trabajo/TK - Vision Artificial/Imagenes/coche.jpeg"
getText(input1)
input2 = "/Users/mentxaka/Documents/Trabajo/TK - Vision Artificial/Imagenes/matricula.jpeg"
getText(input2)
input3 = "/Users/mentxaka/Documents/Trabajo/TK - Vision Artificial/Imagenes/audiq7.jpeg"
getText(input3)
