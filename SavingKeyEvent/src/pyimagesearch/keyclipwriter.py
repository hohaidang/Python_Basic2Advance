'''
Created on Dec 24, 2019

@author: prnsoft
'''
from collections import deque
from threading import Thread
from queue import Queue
import time
import cv2

class KeyClipWriter:
    def __init__(self, bufSize=64, timeout=1.0):
        self.bufSize = bufSize
        self.timeout = timeout
        
        self.frames = deque(maxlen = bufSize)
        self.Q = None
        self.writer = None
        self.thread = None
        self.recording = False
        
    def update(self, frame):
        # update the frames buffer
        self.frames.appendleft(frame)
        
        # if we are recording, update the queue as well
        if self.recording:
            self.Q.put(frame)
            
    def start(self, outputPath, fourcc, fps):
        # indicate that we are recording, start the video writer,
        # and initialize the queue of frames that need to be written to the
        # video file
        self.recording = True
        self.writer = cv2.VideoWriter(outputPath, fourcc, fps,
                (self.frames[0].shape[1], self.frames[0].shape[0]), True)
        self.Q = Queue()
        
        # loop over the frames in the deque structure and add them
        # to the queue
        for i in range(len(self.frames), 0, -1):
            self.Q.put(self.frames[i - 1])
            
        # start a thread write frames to the video file
        self.thread = Thread(target=self.write, args=())
        self.thread.daemon = True
        self.thread.start()