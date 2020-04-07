'''
Created on Dec 10, 2019

@author: prnsoft
'''
# USAGE
# python frame_counter.py --video videos/jurassic_park_trailer.mp4

# import the necessary packages
from imutils.video import count_frames
import argparse
import os

# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-v", "--video", required=True,
#     help="path to input video file")
# ap.add_argument("-o", "--override", type=int, default=-1,
#     help="whether to force manual frame count")
# args = vars('jurassic_park_trailer.mp4')

# count the total number of frames in the video file
override = False
total = count_frames('GH090023.MP4', override=False)

# display the frame count to the terminal
print("[INFO] {:,} total frames read from {}", total)


if __name__ == '__main__':
    pass