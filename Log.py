
"""
Md Tahmid Ahmed
mdtahmid9511@gmail.com
"""
import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

img= cv2.imread('Lena-original-gray (1).png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('input image', img)

print(img.max())
print(img.min())

for i in range (img.shape[0]):
    for j in range (img.shape[1]):
        a = img.item(i,j)
            
        k=math.log(a+1,2)
        c=31
        image = c * k
        img.itemset((i, j),image)
            
cv2.imshow('output image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()