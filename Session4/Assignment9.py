import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def mouse(event,x,y,flags,params):

    if event == cv2.EVENT_LBUTTONDOWN:
        #Debugged by interchanging the places of y and x
        print(frame[y,x]) 
        

cv2.namedWindow('img')

cv2.setMouseCallback('img',mouse)

while True:
    x,frame = cap.read()

    cv2.imshow('img',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break