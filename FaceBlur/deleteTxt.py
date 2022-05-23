import os
import glob

path = '/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/dataSet/images'

numbers = "/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/dataSet/noAnnotations.txt"

lista = list()
# Python mejor que R
# Pasar a Citon

with open(numbers) as f:
    for i in f.readlines():
        lista.append(int(i))
f.close()

for i in lista:
    try:
        file = path + "/" + str(i) +".jpg"
        os.remove(file)
    except:
        print(str(i) + " Tiene anotaciones")