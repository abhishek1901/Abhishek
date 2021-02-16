import cv2
import numpy as np
import random

img = np.zeros((500,500))

width = 500
height = 500

h = int(height/7)
w = int(width/7)

x=0
y=0

def right(x,y):
    while x<=width:
        points = np.array(([x,y],[x+w,y+h]),np.float32)
        cv2.polylines(img,[points],True,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
        x=w

while y<=height:

    right(x,y)

    y=y+h

cv2.imshow('frame',img)

cv2.waitKey(10000)    

