import numpy as np
import cv2
import cv2.aruco as aruco
from collections import OrderedDict
import time

from ColorTracker import *
from ARTracker import *


# CV Callback
def onMouse (event, x, y, f, other):
    # Bring the image from the global context
    global col_tracker

    # print("x:{}  y:{},  color = {}".format(x,y, image[y][x]))
    # Set thy callback event
    if (event == cv2.EVENT_LBUTTONDOWN):
        col_tracker.tracked_colors.append( col_tracker.shifted[y][x] )


def main():

    global col_tracker
    # Create NamedWindow, and set callback.
    cv2.namedWindow('Corrected Perspective')
    cv2.setMouseCallback('Corrected Perspective', onMouse, 0 );

    # Initialize color tracking object
    # Initialize camera input
    cap = cv2.VideoCapture(1)

    # Create the marker tracker object.
    ar_tracker = ARTracker()
    col_tracker = ColorTracker()

    while (1):

        # Capture frame-by-frame
        ret, frame = cap.read()

        # Run the Color Tracker.
        start_time = time.time()
        # Take the current frame and warp it.
        warped = ar_tracker.run(frame)
        # Then track the balls.
        tracked_balls = col_tracker.run(warped)
        end_time = time.time()

        # Draw the amount of tracked balls.
        cv2.putText(warped, "Tracked Balls = {}".format(len(tracked_balls)), (2, 22), cv2.FONT_HERSHEY_SIMPLEX,0.8, (255, 255, 255), 2)

        ## Draw the tracked contours on screen
        for ball in tracked_balls:
            # Draw a circle around each ball
            center = ball[0]
            radius = ball[1]
            color = col_tracker.RGB_dictionary[ball[2]]
            cv2.circle(warped,center,radius,(color[2], color[1], color[0]),2)

            # Draw a white dot at the center of each ball
            cv2.circle(warped, center, 1, (255, 255, 255), -1)

        # Calculate speed of the algorithm
        cv2.putText(warped, "FPS = {}".format(round(1/(end_time-start_time),1)), (2, warped.shape[0]-2), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)

        # Redraw the Image
        cv2.imshow("Original", frame)
        cv2.imshow("Corrected Perspective",  warped)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
