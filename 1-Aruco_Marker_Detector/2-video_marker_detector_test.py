import numpy as np
import cv2
import cv2.aruco as aruco


cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # print(frame.shape) #480x640
    # Our operations on the frame come here
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_1000)
    parameters =  aruco.DetectorParameters_create()


    '''    detectMarkers(...)
        detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
        mgPoints]]]]) -> corners, ids, rejectedImgPoints
        '''

    # Detect Markers and print the corners of the found ones
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    print(corners)

    # Drame the found markers in the image, and show the image.
    frame = aruco.drawDetectedMarkers(frame, corners, ids)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
