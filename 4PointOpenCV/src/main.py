'''
Created on Dec 13, 2019

@author: prnsoft
'''

import numpy as np
import cv2
from transfrom import four_point_transform
import argparse

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", help = "path to the image file")
# ap.add_argument("-c", "--coords",
#     help = "comma seperated list of source points")
# args = vars(ap.parse_args())
 
# load the image and grab the source coordinates (i.e. the list of
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts I'll show you how to
# automatically determine the coordinates without pre-supplying them
image = cv2.imread('example_03.png')
pts = np.array(eval("[(63, 242), (291, 110), (361, 252), (78, 386)]"), dtype = "float32")

warped = four_point_transform(image, pts)
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)

if __name__ == '__main__':
    pass