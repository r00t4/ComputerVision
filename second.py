import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("./shah.jpg",0)
img = cv2.medianBlur(img, 3)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threash = cv2.threshold(img, 125,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU) # why works with retval??


th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 141, 21)
th2 = cv2.medianBlur(th2, 3)
img = cv2.adaptiveThreshold(th2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 141, 21)
#th21 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 2)
# retval2, th24 = cv2.threshold(img, 180,255,cv2.THRESH_OTSU)
# th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('original', img)
cv2.imshow('threash binary', threash)
cv2.imshow('adaptive', th2)
# cv2.imshow('adaptive main', th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
