'''
Created on Dec 24, 2019

@author: prnsoft
'''
 
from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2

# ap = argparse.ArgumentParser()
# ap.add_argument("-o", "--output", required = True,
#                 help="path to output video file")
# ap.add_argument("-p", "--picamera", type = int, default = -1,
#                 help="whether or not the RaspberryPI camera should be used")
# ap.add_argument("-f", "--fps", type=int, default = 20,
#                 help="FPS of output video")
# ap.add_argument("-c", "--codec", type=str, default="MJPG",
#                 help="codec of output video")
# args = vars(ap.parse_args())
 
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
writer = None
(h, w) = (None, None)
zeros = None
 
vidcap = cv2.VideoCapture('jurassic_park_intro.mp4')
# loop over frames from the video stream
while True:
    # grab the frame from the video stream and resize it to have a
    # maximum width of 300 pixels
    (success, frame) = vidcap.read()
    frame = imutils.resize(frame, width=300)
     
    # check if the writer is None
    if writer is None:
        (h, w) = frame.shape[:2]
        """
        cv2.VideoWriter se truyen vao 4 tham so
        1. --output: output name path
        2. fourcc: fourcc codec
        3. FPS: frame per second for video output
        4. (width, height)
        5 Color frame (True: write color, False: not write color)
        """
        writer = cv2.VideoWriter("tenten.avi", fourcc, 20, 
                                 (w * 2, h * 2), True)
        zeros = np.zeros((h, w), dtype="uint8")

    # (B, G, R) is split from frame related to Blue, Green, red    
    (B, G, R) = cv2.split(frame)
    R = cv2.merge([zeros, zeros, R])
    G = cv2.merge([zeros, G, zeros])
    B = cv2.merge([B, zeros, zeros])
         
    # Sap xep vi tri cho video moi.
    output = np.zeros((h * 2, w * 2, 3), dtype = "uint8")
    output[0:h, 0:w] = frame
    output[0:h, w:w * 2] = R
    output[h:h * 2, w:w * 2] = G
    output[h:h * 2, 0:w] = B
         
    writer.write(output)
     
    cv2.imshow("Frame", frame)
    cv2.imshow("Output", output)
    key = cv2.waitKey(1) & 0xFF
     
    if key == ord("q"):
        break
     
print("INFO cleanning up...")
cv2.destroyAllWindows()
writer.release()
         
# python write_to_video.py --output example.avi
# python write_to_video.py --output example.avi --picamera 1
# success, image = vidcap.read()


 
 
if __name__ == '__main__':
    pass