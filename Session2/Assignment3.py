import cv2
import numpy as np

img = cv2.imread('Desktop\dog.jpeg')

w = img.shape[0]
h = img.shape[1]

cv2.line(img,(0,0),(w,h),(255,0,0),5)

cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.imshow('frame',img)
cv2.waitKey(0)



     
