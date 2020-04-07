'''
Created on Dec 10, 2019

@author: prnsoft
'''

import imutils
import cv2

# image = cv2.imread("frame13.jpg")
image = cv2.imread("tetris_blocks.png")
(h, w, d) = image.shape
# (B, G, R) = image[100, 50]
# print("R={}, G={}, B={}".format(R, G, B))
# print("width={}, height={}, depth={}".format(w, h, d))
# 
# roi = image[60:700, 100:420]
# 
# cv2.imshow("Image", roi)
# cv2.waitKey(0)



# r = 300.0 / w
# dim = (300, int(h * r))
# resized = cv2.resize(image, dim)
# cv2.imshow("Aspect Ratio Resize", resized)
# cv2.waitKey(0)



output = image.copy()
cv2.rectangle(output, (20, 12), (254, 58), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# -------------------Detect edge-----------------------
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray)
# edged = cv2.Canny(gray, 30, 150)
# cv2.imshow("Edge", edged)
# thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
# cv2.imshow("Thresh", thresh)
# -------------------------------------------------------

# ------------------Detecting and drawing contours---------------
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# output = image.copy()
# 
# for c in cnts:
#     cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
#     cv2.imshow("Contours", output)
#     cv2.waitKey(0)
# ----------------------------------------------------------------
    
# ------------------Erosions and dilations---------------
# mask = thresh.copy()
# cv2.imshow("thresh1", mask)
# mask = cv2.erode(mask, None, iterations = 5)
# cv2.imshow("erode", mask)
# mask = cv2.dilate(mask, None, iterations = 5)
# cv2.imshow("dilate", mask)
# # ----------------------------------------------------------------
# cv2.waitKey(0)


if __name__ == '__main__':
    pass