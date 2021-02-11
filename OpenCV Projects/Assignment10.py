import cv2
import numpy as np

img = cv2.imread('dog.jpeg')

a = False
b = False

def crop(event,x,y,flags,param):

    global pts,a,b

    if event == cv2.EVENT_LBUTTONDOWN:

        if a == False:
            pts = [(x,y)]
            a = True
        elif b == False:
            pts.append((x,y))
            b=True
        if len(pts) == 2:
            y1,y2,x1,x2 = pts[0][1],pts[1][1],pts[0][0],pts[1][0]
            cropped = img[y1:y2,x1:x2]
            cv2.imshow('frame',cropped)
            cv2.waitKey(0)

cv2.namedWindow('frame')

cv2.setMouseCallback('frame',crop)

cv2.imshow('frame',img)
cv2.waitKey(0)
   