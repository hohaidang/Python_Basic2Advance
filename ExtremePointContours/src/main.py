'''
Created on Dec 17, 2019

@author: prnsoft
'''

import imutils
import cv2

image = cv2.imread("hand_01.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

thres = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thres = cv2.erode(thres, None, iterations = 2)
thres = cv2.dilate(thres, None, iterations = 2)

cnts = cv2.findContours(thres.copy(), cv2.RETR_EXTERNAL, 
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# lay contour to nhat
c = max(cnts, key=cv2.contourArea) # Lay max contour de khu nhieu

# Lay nhung diem cuc tri
extLeft = tuple(c[c[:, :, 0].argmin(), 0]) # Lay diem cuc tri ben trai bang cach lay min cua truc X
extRight = tuple(c[c[:, :, 0].argmax(), 0]) # cuc dai X
extTop = tuple(c[c[:, :, 1].argmin(), 0]) # cuc tieu Y
extDown = tuple(c[c[:, :, 1].argmax(), 0]) # cuc dai Y

cv2.drawContours(image, [c], -1, (0, 255, 255), 2)

cv2.circle(image, extLeft, 8, (0, 0, 255), -1)
cv2.circle(image, extRight, 8, (0, 255, 0), -1)
cv2.circle(image, extTop, 8, (255, 0, 0), -1)
cv2.circle(image, extDown, 8, (255, 255, 0), -1)



cv2.imshow("Output", image)
cv2.waitKey(0)

if __name__ == '__main__':
    pass