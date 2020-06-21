import cv2
import numpy as np

def nothing(x):
    pass


cap = cv2.VideoCapture(0)
cv2.namedWindow('image')

cv2.createTrackbar('H','image',0,180,nothing)
cv2.createTrackbar('S','image',0,255,nothing)
cv2.createTrackbar('V','image',0,255,nothing)


while(1):
    ret,frame = cap.read()

    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    h = cv2.getTrackbarPos('H','image')
    s = cv2.getTrackbarPos('S','image')
    v = cv2.getTrackbarPos('V','image')
    


    thresh_low = np.array([h,s,v])
    thresh_high = np.array([180,255,255])

    mask =cv2.inRange(frame_hsv,thresh_low,thresh_high)
    
    res = cv2.bitwise_and(frame,frame, mask = mask)

    cv2.imshow('image',frame)
    cv2.imshow('image2',res)

    if cv2.waitKey(1) & 0xFF == 27:
        break




   
    







