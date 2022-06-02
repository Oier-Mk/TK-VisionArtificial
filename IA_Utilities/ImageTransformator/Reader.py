import cv2 as cv
import pytesseract

def reader(path):
  img_read = cv.imread(path)
  grayscale = cv.cvtColor(img_read, cv.COLOR_BGR2GRAY)
  extractedInformation = pytesseract.image_to_string(grayscale)
  return extractedInformation
