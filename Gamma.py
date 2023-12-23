"""
Md Tahmid Ahmed
mdtahmid9511@gmail.com
"""
import numpy as np
import cv2

img = cv2.imread('grayscale-image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('input image', img)

print(img.max())
print(img.min())

gamma = 0.5

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        a = img.item(i, j)
        image = int(a**gamma) 
        img.itemset((i, j), image)

cv2.imshow('output image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
