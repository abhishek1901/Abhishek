import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('20200627_102116_mfnr.jpg')
img1 = cv2.resize(img,(500,500))
cv2.namedWindow('image')

cv2.createTrackbar('H','image',1,256,nothing)



while(1):
    im_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    

    #frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lut = cv2.getTrackbarPos('H','image')
    im_color = cv2.LUT(im_gray,lut)
    


    thresh_low = np.array([h])
    thresh_high = np.array([1,256])

    mask =cv2.inRange(im_color,thresh_low,thresh_high)
    
    res = cv2.bitwise_and(img_color,im_color, mask = mask)

    cv2.imshow('image',im_color)
    cv2.imshow('image2',res)

    if cv2.waitKey(1) & 0xFF == 27:
        break




   
    







