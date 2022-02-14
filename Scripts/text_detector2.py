import os
import argparse
import time
import cv2
import pytesseract
import re 
import traceback


def textDetect(file):
    path = file.split("/")
    nombre = path[-1]
    nombre = nombre.split(".")[0]
    path.pop(-1)
    path = "/".join(path)
    img = cv2.imread(file)
    img_final = img.copy()
    
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       # Pasa a gris    
    blur = cv2.GaussianBlur(img2gray, (3,3), 0)            # Filtro de desenfoque para limpiar ruido 
    ret, mask = cv2.threshold(blur, 180, 255, cv2.THRESH_BINARY)   # Binarización agresiva para generar una mascara
    masked_img = cv2.bitwise_and(blur, blur, mask=mask)            # Se hace un AND de la imagen consigo misma aplicando la mascara
    ret, new_img = cv2.threshold(masked_img, 180, 255, cv2.THRESH_BINARY) # Binariza la imagen resultante del AND y se invierte
    # Solo para debug mostramos los pasos
    #cv2.imwrite('mascara.jpg',mask)
    #cv2.imwrite('imagen_para_contornos.jpg',new_img)

    # Se obtienen los contornos de la imagen. Un contorno es una curva que une puntos continuos por tener el mismo color o intensidad
    contours, hierarchy = cv2.findContours(new_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    ROI_number = 0

    if not os.path.isdir(path+"/rectangulos"):
        os.mkdir(path+"/rectangulos")
    path += "/rectangulos"
    if not os.path.isdir(path+"/rectangulos_"+nombre):
        os.mkdir(path+"/rectangulos_"+nombre)

    for contour in contours:
        [x, y, w, h] = cv2.boundingRect(contour)    # Se obtiene el rectangulo que contiene el contorno
        if w < 35 and h < 35:                       # Se filtran contornos que no son muy grandes
            continue

        if w>h*2:    # Se buscan matriculas. Nos interesan contornos cuyo ancho sea mayor que el doble de la altura            

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)    # Pintamos todos los contornos sobre la imagen original
            

            # TODO: Hacer crop de los contornos, pasar OCR sobre ellos y ver el que nos devuelve texto
            ROI = new_img[y:y+h, x:x+w]

            destino = path+"/rectangulos_"+nombre+'/imagen_{}.png'.format(ROI_number)
            cv2.imwrite(destino, ROI)
            cv2.rectangle(img,(x,y),(x+w,y+h),(36,255,12),2)
            ROI_number += 1



def readText(path):
    print(path)
    img_read = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    extractedInformation = pytesseract.image_to_string(img_read)
    return extractedInformation



def textRecognition(path):
    #formo una lista con las imagenes de la ultima carpeta creada
    listadeimagenes = os.listdir(path)

    print(listadeimagenes)

    extractedInformation = "Imprimimos la matricula\n"

    for i in listadeimagenes: 
        try:
            pathAbsoluto = path + "/" + i            
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
            print("no se ha podido leer texto de la imagen "+ i.split('/')[-1])


    print(extractedInformation)



'''
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", type=str, default=None, required=True, help="Image file to detect text regions")
    args = ap.parse_args()

    input_file = args.file
    if args.file:
        if not args.file.startswith(os.sep):
            input_file = os.path.join(os.getcwd(), args.file)
        if not os.path.exists(input_file):
            print("Could not find file '{}'".format(input_file))
            return
    textDetect(input_file)



if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Process complete in {0:.2f} seconds".format(end-start))

'''

'''

#FUNCIONA, SACA TODOS LOS RECTANGULOS

path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/Imagenes/coches/"

listadeimagenes = os.listdir(path)

print(listadeimagenes)

for i in listadeimagenes:
    try:
        textDetect(path+i)
    except:
        traceback.print_exc()
        print("no se ha podido detectar nada en  " + i)

'''

path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/Imagenes/coches/rectangulos/"

listadedirectorios = os.listdir(path)

for i in range(len(listadedirectorios)):
    directorioPath = path+listadedirectorios[i]
    textRecognition(directorioPath)
  