# USAGE
# python read_frames_slow.py --video videos/jurassic_park_intro.mp4

# import the necessary packages
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import cv2

stream = cv2.VideoCapture('jurassic_park_intro.mp4')
fps = FPS().start()

# loop over frames from the video file stream
while True:
    # grab the frame from the threaded video file stream
    (grabbed, frame) = stream.read()

    # if the frame was not grabbed, then we have reached the end
    # of the stream
    if not grabbed:
        break

    # resize the frame and convert it to grayscale (while still
    # retaining 3 channels)
    frame = imutils.resize(frame, width=450)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = np.dstack([frame, frame, frame])

    # display a piece of text to the frame (so we can benchmark
    # fairly against the fast method)
    cv2.putText(frame, "Slow Method", (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)    

    # show the frame and update the FPS counter
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
    fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
stream.release()
cv2.destroyAllWindows()