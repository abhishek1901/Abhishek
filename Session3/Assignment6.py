import cv2
import numpy as np
import random

img = cv2.imread('dog.jpg')

width = print (img.shape[1])
height = print (img.shape[0])

h = int(height/7)
w = int(width/7)

x=0
y=0

def right(x,y):
    while x<=width:
        cv2.rectangle(img,(x,y),((x+w),(y+h)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
        x=w

while y<=height:

    right(x,y)

    y=y+h

cv2.imshow('frame',img)

cv2.waitKey(10000)    

