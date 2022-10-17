import glob
import traceback
from leer_texto import prepareReadEasy, readEasy
import os
import re

relative = os.getcwd() #local

def textReading(path,reader):   
    print("Lectura del OCR comenzada")
    #folder reading
    results = glob.glob(path)
    results.sort()
    lecturaNombre = []
    lecturaResultado = []
    for image in results:
        try:
            #lectura de matricula
            lecturaNombre.append(image.split(os.path.sep)[-1])
            prov = ""
            lecturas = readEasy(reader, image)
            for text in lecturas:
                prov+=text[1]
            lecturaResultado.append(prov)
            print("la imagen "+image.split(os.path.sep)[-1]+" SI tiene matrículas legibless")
        except Exception:
            print(traceback.format_exc())
            print("la imagen "+image.split(os.path.sep)[-1]+" NO tiene matrículas legibless")
    print("Lectura del OCR completada")

    return(lecturaNombre,lecturaResultado)

def regExp(lecturaNombre,lecturaResultado): 

    lecturaResultado = remSpace(lecturaResultado)

    lecturaNombre,lecturaResultado = deleteIncorrectPlates(lecturaNombre,lecturaResultado)
    
    lecturaNombre,lecturaResultado = remEquals(lecturaNombre,lecturaResultado)

    prov = "" 
    for i, name in enumerate(lecturaNombre): 
        prov += (name +"\t"+lecturaResultado[i] +"\n")
    
    pathText = relative + os.path.sep + "results" + os.path.sep + "log.txt" 
    with open(pathText, 'w') as f:
        f.write(prov)

    print("txt generado")

def getRepIndexes(array, element):
    indexes = [] 
    if element not in array: return None
    for idx, ele in enumerate(array):
        if (element == ele): indexes.append(idx)
    return indexes

def remSpace(lecturaResultado):
    print("borrando espacio")
    prov = []
    for idx, plate in enumerate(lecturaResultado):
        prov.append(plate.replace(" ",""))
    lecturaResultado = prov
    print("espacios borrados")
    return(lecturaResultado)


def remEquals(lecturaNombre, lecturaResultado):
    print("borrando iguales")
    for plate in lecturaResultado:
        indexes = getRepIndexes(lecturaResultado, plate)
        indexes.pop(0)
        for i,idx in enumerate(indexes):
            lecturaResultado.pop(idx-i)
            lecturaNombre.pop(idx-i)
    print("iguales borrados")
    return(lecturaNombre,lecturaResultado)
        

def deleteIncorrectPlates(lecturaNombre,lecturaResultado):    
    provNombre = []
    provResultado = []
    for idx, val in enumerate(lecturaResultado):
        match = re.search('([1234567890]{4})([BCDFGHJKLMNPQRSTWXYZ]{3})', val) 
        if match:
            print(f"YES! We have a match! idx = {idx} $$ val = {lecturaResultado[idx]}")
            provNombre.append(lecturaNombre[idx])
            provResultado.append(lecturaResultado[idx])

    print(provResultado)
    return(provNombre,provResultado)
    
reader = prepareReadEasy() 

path = relative + os.path.sep + "results" + os.path.sep + "crops" + os.path.sep + "*" 
lecturaNombres, lectureResultados = textReading(path,reader)
regExp(lecturaNombres, lectureResultados)