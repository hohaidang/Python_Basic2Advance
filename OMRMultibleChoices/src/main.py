'''
Created on Dec 18, 2019

@author: prnsoft
'''
import cv2
import numpy as np
import imutils
from imutils import contours
from imutils.perspective import four_point_transform
from numpy import dtype

ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}

image = cv2.imread('test_01.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
docCnt = None

# Tim vien cua to giay thi
if len(cnts) > 0:
    # sort decesnding order
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)
    
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        
        if len(approx) == 4:
            docCnt = approx
            break
# Cat hinh "bird eye view"        
paper = four_point_transform(image, docCnt.reshape(4, 2))
warped = four_point_transform(gray, docCnt.reshape(4, 2))

# THRESH_BINARY_INV se doi nguoc lai, nhung bien != 0 se mau den (=0), nhung bien = 0 se mau trang ( = 255)
# OTSU la thuat toan de tim ra diem sang toi (https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html) 
thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cv2.imshow("thesh", thresh)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
questionCnts = []

for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    aspectRatio = w / float(h)
    
    # de chac do la 1 cau tra loi thi
    # width >= 20 & h >= 20 & ti le chia nhau gan = 1 (hinh tron)
    if w >= 20 and h >= 20 and aspectRatio >= 0.9 and aspectRatio <= 1.1:
        questionCnts.append(c)


# Sap xep thu tu tu` tren xuong 
questionCnts = contours.sort_contours(questionCnts, method="top-to-bottom")[0]
correct = 0

# moi hang se co 5 cau hoi, vay se loop moi hang, roi sap xep thu tu tung cau hoi
for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
    # questionCnts[0:5], questionCnts[5:10], ... cu nhu vay loop het 20 cau hoi 
    cnts = contours.sort_contours(questionCnts[i: i + 5])[0]
    bubbled = None
    for (j, c) in enumerate(cnts):
        mask = np.zeros(thresh.shape, dtype="uint8")
        # to dam mat na cho tung cau hoi
        cv2.drawContours(mask, [c], -1, 255, -1)
        # tao mat na cho tung o
        mask = cv2.bitwise_and(thresh, thresh, mask=mask)
        # Dem so pixels dang = 255
        total = cv2.countNonZero(mask)
        
        # tim diem dc to, luu vao bubble
        if bubbled is None or total > bubbled[0]:
            bubbled = (total, j) # neu pixels nhieu nhat (tuc la cau tra loi dc boi den)
            
    color = (0, 0, 255)
    # k la dap an
    k = ANSWER_KEY[q] # q la thu tu cau hoi 1, 2, 3, 4, 5
        
    if k == bubbled[1]: # bubbled[1] tuc la cau tra loi duoc boi den (pixels lon nhat) == dap an
        color = (0, 255, 0) # neu dung khoanh mau xanh
        correct += 1
        
    # neu khong dung thi color van giu nguyen la mau do
    cv2.drawContours(paper, [cnts[k]], -1, color, 3)

    
score = (correct / 5.0) * 100
print("[INFO] score: {:.2f}%".format(score))
cv2.putText(paper, "{:.2f}%".format(score), (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
cv2.imshow("paper", paper)
cv2.imshow("warped", warped)
cv2.waitKey(0)



if __name__ == '__main__':
    pass