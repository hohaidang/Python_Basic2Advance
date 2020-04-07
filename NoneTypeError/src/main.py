'''
Created on Dec 17, 2019

@author: prnsoft
'''
import cv2

# Neu khong co hinh, thi ham imread se tra ve None
image = cv2.imread('example.png')
# print(image.shape) # Khi print mot bien None se bi bao loi
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # AssertionError se duoc quang ra boi vi image la None


if __name__ == '__main__':
    pass