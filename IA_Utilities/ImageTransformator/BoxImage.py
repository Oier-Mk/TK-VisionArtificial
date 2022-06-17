
import numpy as np
import cv2
import os

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized

# Clasifica los cuatro vértices del contorno obtenido en el paso anterior en el orden de arriba a la izquierda, arriba a la derecha, abajo a la derecha, abajo a la izquierda
def order_points(pts):
    # Un total de 4 puntos de coordenadas
    rect = np.zeros((4, 2), dtype = "float32")

    # Encuentra las coordenadas correspondientes 0123 en orden superior izquierda, superior derecha, inferior derecha, inferior izquierda
    # Calcular arriba a la izquierda, abajo a la derecha
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # Calcular arriba a la derecha y abajo a la izquierda
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect

# Transformación de perspectiva.
def four_point_transform(image, pts):
    # Obtener coordenadas de entrada
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # Calcular los valores de entrada w y h
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # Posición de coordenadas correspondiente después de la transformación (-1 es solo para evitar errores, no -1 también es posible).
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")

    # Calcular la matriz de transformación
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    # Devuelve el resultado transformado
    return warped

def boxImage(input):
  import numpy as np
  import cv2
  import os

  # Leer entrada
  image = cv2.imread(input)
  # Las coordenadas también cambiarán lo mismo
  ratio = image.shape[0] / 500.0
  orig = image.copy()
  image = resize(orig, height = 500)

  # Preprocesamiento
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (5, 5), 0)  # Filtrado gaussiano
  edged = cv2.Canny(gray, 75, 200)  # Detección de bordes canny

  # Detección de contorno (el contorno con el área más grande probablemente sea el contorno que necesitamos).
  cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
  cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

  # Recorrer el contorno
  for c in cnts:
      # Calcular aproximación de contorno
      peri = cv2.arcLength(c, True)
      # c indica el conjunto de puntos de entrada
      # epsilon representa la distancia máxima desde el contorno original hasta el contorno aproximado, es un parámetro de precisión
      # Verdadero significa cerrado
      approx = cv2.approxPolyDP(c, 0.02 * peri, True)

      # Sácalo en 4 puntos
      if len(approx) == 4:
          screenCnt = approx
          break
  
  cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
  
  # Transformación de perspectiva
  warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
  # Procesamiento binario
  warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
  ref = cv2.adaptiveThreshold(warped, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)
  return ref

