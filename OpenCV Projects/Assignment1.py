import cv2
import numpy as np


img = cv2.imread('IMG_3879.jpg')
img_1=cv2.resize(img,(500,500))
img_gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
img_gray_smooth = cv2.GaussianBlur(img_gray,(5,5),0)
ret,img_gray_smooth_thresh = cv2.threshold(img_gray_smooth,180,300,cv2.THRESH_BINARY)
print(img_gray_smooth_thresh)
cv2.imshow('frame',img_gray_smooth_thresh)
cv2.waitKey(0)