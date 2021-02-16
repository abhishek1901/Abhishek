import cv2
import numpy as np

img = cv2.imread('dog.jpeg')

kernel = np.zeros((3,3))

kernel[0,1] = -1
kernel[1,2] = -1
kernel[2,1] = -1
kernel[1,2] = -1
kernel[1,1] = 4

imd = cv2.filter2D(img,-1,kernel)

cv2.imshow('frame',img)

cv2.waitKey(0)

     