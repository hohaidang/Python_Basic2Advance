'''
Created on Dec 6, 2019

@author: prnsoft
'''

import cv2
import numpy as np
from cv2 import imshow

img = cv2.imread('input_train.jpg', cv2.IMREAD_GRAYSCALE)
sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
canny = cv2.Canny(img, 10, 240)

cv2.imshow('Canny', canny)
# cv2.imshow('Laplacian', laplacian)
# cv2.imshow('Original', img)
# cv2.imshow('Sobel horizontal', sobel_horizontal)
# cv2.imshow('Sobel vertical', sobel_vertical)


cv2.waitKey()
if __name__ == '__main__':
    pass