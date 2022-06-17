# Import libraries
import cv2 as cv

def deleteLines(image, horizontal = True, vertical = True):
  # Read the original image
  img = cv.imread(image)
  img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  #invertimos el color de la imagen y aplicamos un threshold adaptativo
  img_inv = cv.bitwise_not(img_gray)
  img_thresh = cv.adaptiveThreshold(img_inv, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 15, -2)
  img_thresh_inv = (255- img_thresh)

  if(horizontal):
    # Remove horizontal
    horizontal_kernel = cv.getStructuringElement(cv.MORPH_RECT, (25,1))
    detected_lines = cv.morphologyEx(img_thresh, cv.MORPH_OPEN, horizontal_kernel, iterations=2)
    cnts = cv.findContours(detected_lines, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv.drawContours(img_thresh_inv, [c], -1, (255,255,255), 2)
  if(vertical):
    # Remove vertical
    vertical_kernel = cv.getStructuringElement(cv.MORPH_RECT, (1,25))
    detected_vert_lines = cv.morphologyEx(img_thresh, cv.MORPH_OPEN, vertical_kernel, iterations=2)
    cnts2 = cv.findContours(detected_vert_lines, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts2 = cnts2[0] if len(cnts2) == 2 else cnts2[1]
    for c2 in cnts2:
        cv.drawContours(img_thresh_inv, [c2], -1, (255,255,255), 2)

  return img_thresh_inv
