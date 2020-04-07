'''
Created on Dec 11, 2019

@author: prnsoft
'''
import cv2
import imutils

image = cv2.imread("shapes_and_colors.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# Tao nhung mang contour, va dc danh so thu tu tu` 0 -> 16
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    # compute the center of the contour
    # Ham nay se tinh ra tat ca nhung diem (moment), tu` nhung diem nay ap dung cong thuc tich phan
    # se tinh duoc diem trung tam cua moi hinh hoc va nhieu nua. 
    # https://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html
    # https://en.wikipedia.org/wiki/Centroid
    # https://en.wikipedia.org/wiki/Image_moment
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    
    # draw the contour and center of the shape on the image
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2) # Ve Contour nho` vao tung counter da duoc tach ra
    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1) # Ve hinh tron trong tung tam contour
    cv2.putText(image, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255) , 2)
    
    cv2.imshow("Image", image)
    cv2.waitKey(0)
# cv2.imshow("thresh", cnts)
# cv2.waitKey(0)

if __name__ == '__main__':
    pass