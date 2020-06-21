import cv2
import numpy as np

img = cv2.imread('IMG_3879.jpg')

img_resize = cv2.resize(img,(700,700))

img_gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)

med_val = np.median(img_resize)

thres1 = int(max(0,0.7*med_val))
thres2 = int(max(255,1.3*med_val))

edged = cv2.Canny(img_gray,thres1,thres2)

contours,hierarchy = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#print(contours)
area = [cv2.contourArea(c) for c in contours]

max_index = np.argmax(area)
max_contour = contours[max_index]

perimeter = cv2.arcLength(max_contour,True)

Roi = cv2.approxPolyDP(max_contour,0.01*perimeter,True)
#print(Roi)

#x,y,w,h = cv2.boundingRect(max_contour)

#cropped = img_resize[y:h,x:w]

pt1 = np.array([Roi[1],Roi[0],Roi[2],Roi[3]],np.float32)
pt2 = np.array([(0,0),(500,0),(0,500),(500,500)],np.float32)
#print(pt2)

perspective = cv2.getPerspectiveTransform(pt1,pt2)

Transformed = cv2.warpPerspective(img_resize,perspective,(500,500))

#cv2.drawContours(img_resize,[Roi],-1,(0,255,0),5)

#cv2.imshow('frame',img_resize)
cv2.imshow('frame',Transformed)
#cv2.imshow('frame',cropped)

cv2.waitKey(0)

