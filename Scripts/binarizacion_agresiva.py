 # coding=utf-8


def aggressiveBinarization(file):
    try:
        import os
        import cv2
        path = file.split("/")
        path.pop(-1)
        path = "/".join(path)
        img = cv2.imread(file)
        img_final = img.copy()
        img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# Pasa a gris
        blur = cv2.GaussianBlur(img2gray, (3,3), 0)# Filtro de desenfoque para limpiar ruido 
        ret, mask = cv2.threshold(blur, 180, 255, cv2.THRESH_BINARY)# Binarización agresiva para generar una mascara
        masked_img = cv2.bitwise_and(blur, blur, mask=mask)# Se hace un AND de la imagen consigo misma aplicando la mascara
        ret, new_img = cv2.threshold(masked_img, 180, 255, cv2.THRESH_BINARY)# Binariza la imagen resultante del AND y se invierte
        # Solo para debug mostramos los pasos
        if not os.path.isdir(path+"/mascara"):
            os.mkdir(path+"/mascara")

        nuevopath = path+"/mascara/mascara_"+file.split("/")[-1]
        cv2.imwrite(nuevopath,new_img)

        return path+"mascara "+file.split("/")[-1]
    except:
        print("no se ha podido realizar la lectura de la imagen")