import os

#USAMOS ESTE SCRIPT PARA BORRAR AQUELLAS FOTOS QUE NO TENGAN ANOTACIONES, LAS INDICADAS EN EL TXT DE NOANNOTATIONS.TXT

path = "/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/data/train/"

numbers = path+"noAnnotations.txt"

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