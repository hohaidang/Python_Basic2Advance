'''
Created on Dec 16, 2019

@author: prnsoft
'''

from scipy.spatial import distance as dist
import numpy as np
import cv2
import imutils
from imutils import contours
from imutils import perspective
from transfrom import order_points_old



image = cv2.imread("example_01.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)

edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
cv2.imshow("Edged", edged)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

(cnts, _) = contours.sort_contours(cnts)
colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0))


for (i, c) in enumerate(cnts):
    if cv2.contourArea(c) < 100:
        continue
    
    box = cv2.minAreaRect(c)
    box = cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
    
    # New
    rect = perspective.order_points(box)
#     rect = Test_Understanding(box)
#     rect = order_points_old(box)
    
    print(rect.astype("int"))
    print("")
    print("Zip = ", zip(rect, colors))
    for ((x, y), color) in zip(rect, colors):
        cv2.circle(image, (int(x), int(y)), 5, color, -1)
        
    cv2.putText(image, "Object #{}".format(i + 1),
        (int(rect[0][0] - 15), int(rect[0][1] - 15)),
        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)
    
    cv2.imshow("image", image)
    cv2.waitKey(0)
    


cv2.waitKey(0)

if __name__ == '__main__':
    pass