import cv2
import numpy as np

img = cv2.imread('IMG_3879.jpg')

img_new = cv2.resize(img,(600,600))


point = []

def crop(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:

        point.append((x,y))
        if len(point) == 4:
            pts1 = np.array((point[0],point[1],point[2],point[3]),np.float32)

            pts2 = np.array(((0,0),(0,1000),(1000,0),(1000,1000)),np.float32)

            perspective = cv2.getPerspectiveTransform(pts1,pts2)

            transformed = cv2.warpPerspective(img_new,perspective,(500,500))

            cv2.imshow('img1',transformed)

            cv2.waitKey(0)
        


    
cv2.namedWindow('img')

cv2.setMouseCallback('img',crop)

cv2.imshow('img',img_new)
cv2.waitKey(0)
   