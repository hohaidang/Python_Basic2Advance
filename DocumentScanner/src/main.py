'''
Created on Dec 18, 2019

@author: prnsoft
'''
import cv2
import numpy as np
import imutils
from imutils.perspective import four_point_transform
from skimage.filters import threshold_local


image = cv2.imread('page.jpg')
ratio = image.shape[0] / 500.0 
orig = image.copy()
image = imutils.resize(image, height = 500)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

#  ------------------- Cach tim 4 diem cua 1 object hinh chu nhat ---------------
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# func sorted dung de sort contour theo dien tich, reserse = True tuc la sort tu lon nhat -> nho nhat
# [:5] lay 5 contour co dien tich lon nhat
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

for c in cnts:
    # Tinh chieu dai cua contour, True cho biet la contour la contour dong
    peri = cv2.arcLength(c, True)
    # Dung thuat toan lam giam so luong diem tao thanh 1 da giac (duong cong) (https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm)
    # 0.02*peri -> la tham so sap xi giua duong cong ban dau va sap si duong cong moi (voi it diem hon)
    # True -> la duong cong (da giac) co diem dau va diem cuoi noi nhau.
    approx = cv2.approxPolyDP(c, 0.02*peri, True)
    
    # Boi vi la hinh chu nhat, nen chi can 4 diem la ve dc 1 hinh chu nhat, nen approx sau khi toi gian diem se = 4
    if len(approx) == 4:
        screenCnt = approx
        break
    
print("Step2: Find contours of paper")
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
#  -----------------------------------------------------------------------------
# sap xep thu tu 4 diem cua 1 hinh chu nhat
# sau do cat hinh chu nhat ra
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)

# se tra ve 1 ma tran T, T se bao gom tat ca nhung gia tri sau khi qua filter threshold
# block_size va offset la 2 bien can dung de canh chinh bo loc
T = threshold_local(warped, 21, offset = 10, method = "gaussian")
# so sanh vs ma tran T, neu gia tri nao lon hon se chuyen thanh 255
warped = (warped > T).astype("uint8")*255


print("Step 3: Apply perspective transform")
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))


cv2.waitKey(0)
cv2.destroyAllWindows()


if __name__ == '__main__':
    pass