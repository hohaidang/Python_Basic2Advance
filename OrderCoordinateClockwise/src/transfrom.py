'''
Created on Dec 13, 2019

@author: prnsoft
'''
from scipy.spatial import distance as dist
import numpy as np
import cv2
import imutils
from imutils import contours

def order_point(pts):
    xSorted = pts[np.argsort(pts[:, 0]), :]
    leftMost = xSorted[:2, :]
    rightMost = xSorted[2:, :]
    
    leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
    (tl, bl) = leftMost
    
    D = dist.cdist(tl[np.newaxis], rightMost, "eulidean")[0]
    (br, tr) = rightMost[np.argsort(D)[::-1], :]
    
    return np.array([tl, tr, br, bl], dtype="float32")

def order_points_old(pts):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype = "float32")
 
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    
    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis = 1)
    a = np.argmin(diff)
    b = np.argmax(diff)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    
    return rect

def four_point_transform(image, pts):
    
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
#     a = (br[0] - bl[0]) ** 2
    
    # Tinh chieu dai duong thang tu 2 diem
    # Binh phuong gia tri x + y roi lay can bac 2
    widthA = np.sqrt( ((br[0] - bl[0]) ** 2) + ( ((br[1] - bl[1]) ** 2) ) ) 
    widthB = np.sqrt( ((tr[0] - tl[0]) ** 2) + ( ((tr[1] - tl[1]) ** 2) ) )
    maxWidth = max(int(widthA), int(widthB))
    
    heighA = np.sqrt( ((tr[0] - br[0]) ** 2) + ( ((tr[1] - br[1]) ** 2) ) )
    heighB = np.sqrt( ((tl[0] - bl[0]) ** 2) + ( ((tl[1] - bl[1]) ** 2) ) )
    maxHeight = max(int(heighA), int(heighB))
    
    dst = np.array([
        [0, 0], 
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")
    
    M = cv2.getPerspectiveTransform(rect, dst) # Tao ra 1 ma tran tu 4 points src -> 4 points dest
    # Nho ma tran o tren func se tinh toan de cat tam hinh theo 4points + chieu dai, chieu rong
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight)) 
    
    return warped

