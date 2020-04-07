'''
Created on Dec 17, 2019

@author: prnsoft
'''
import cv2
import imutils
import numpy as np


image = cv2.imread('pill_01.png')
# Lay moi diem +15 tu 0 -> 360
# for angle in np.arange(0, 360, 15):
#     rotated = imutils.rotate(image, angle)
#     cv2.imshow("Rotated (Problematic)", rotated)
#     cv2.waitKey(0)


# for angle in np.arange(0, 360, 15):
#     if angle == 0:
#         continue
#     rotated = imutils.rotate_bound(image, angle)
#     cv2.imshow("Rotated (Correct)", rotated)
#     cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 20, 100)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

if len(cnts) > 0:
    c = max(cnts, key=cv2.contourArea)
    mask = np.zeros(gray.shape, dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1) # Do ben trong contour vs gia tri thickness = -1
    
    (x, y, w, h) = cv2.boundingRect(c)
    imageROI = image[y:y + h, x:x + w]
    maskROI = mask[y:y + h, x:x + w]
    imageROI = cv2.bitwise_and(imageROI, imageROI, mask=maskROI)
    cv2.imshow("Output", imageROI)
    


for angle in np.arange(0, 360, 15):
    if angle == 0:
        continue
    rotated = imutils.rotate_bound(imageROI, angle)
    cv2.imshow("Rotated (Correct)", rotated)
    cv2.waitKey(0)

cv2.waitKey(0)

if __name__ == '__main__':
    pass