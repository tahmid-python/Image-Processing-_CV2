# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 15:05:27 2023

@author: Welcome Students
"""
import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

img= cv2.imread('grayscale-image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('input image', img)

print(img.max())
print(img.min())

for i in range (img.shape[0]):
    for j in range (img.shape[1]):
        a = img.item(i,j)
        c=31
        k=a/c
        image =k**2
        img.itemset((i, j),image-1)
cv2.imshow('output image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()