import os
import argparse
import time
import cv2
import pytesseract
import re 
import traceback

def readText(path):
    img_read = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    extractedInformation = pytesseract.image_to_string(img_read, lang='spa', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789BCDFGHJKLMNPQRSTWXYZ')
    return extractedInformation

def textRecognition(path):

    extractedInformation = "Imprimimos la matricula\n"

    try:
        pathAbsoluto = path           
        if os.path.exists(pathAbsoluto) and os.path.isfile(pathAbsoluto):
            txt = readText(pathAbsoluto)
            txt = txt.upper()
            txt = re.sub(r'[^A-Z0-9]', '', txt)
            if (len(txt)>0):
                extractedInformation += txt+"\n"
        else:
            print("No se encuentra el fichero {}".format(pathAbsoluto))
    except:
        traceback.print_exc()
        print("no se ha podido leer texto de la imagen "+ path.split('/')[-1])

    print(extractedInformation)

file = "/Users/mentxaka/Desktop/casoCurioso.png"
textRecognition(file)