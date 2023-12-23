"""
Md Tahmid Ahmed
mdtahmid9511@gmail.com
"""

import numpy as np
import cv2
import math

img= cv2.imread('grayscale-image.jpg', cv2.IMREAD_GRAYSCALE)


kernel = np.ones((7, 7), np.uint8)

#img_erosion = cv2.erode(img, kernel, iterations=3)
img_dilation = cv2.dilate(img, kernel, iterations=3)


cv2.imshow('input image', img)
#cv2.imshow('Erosion image', img_erosion)
cv2.imshow('Dilation image', img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()

