import cv2
import numpy as np

img = cv2.imread('IMG_3879.jpg')

img_reshape = cv2.resize(img,(700,700))

med_val = np.median(img)

threshold1 = int(max(0,0.2*med_val))

threshold2 = int(max(0,1.8*med_val))

blurred_img = cv2.blur(img_reshape,ksize=(8,8))

edges = cv2.Canny(blurred_img,threshold1,threshold2)

cv2.imshow('frame',img_reshape)
cv2.waitKey(0)

cv2.imshow('frame1',edges)
cv2.waitKey(0)