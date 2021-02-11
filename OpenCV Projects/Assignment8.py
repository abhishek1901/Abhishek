import cv2
import random

img = cv2.imread('dog.jpg')

width = img.shape[1]

height = img.shape[0]

h = int(height/7)
w = int(width/7)

x=0
y=0

def right(x,y):
    new = img.copy()
    while x<=width:
        cv2.rectangle(img,(x,y),((x+w),(y+h)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
        x+=w
        cv2.imshow('frame',img)
        cv2.waitKey(100) 
        left(x,y+(h+2)) 


def left(x,y):
    new = img.copy()
    while x>=0:
        cv2.rectangle(img,(x,y),((x+w),(y+h)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
        x+=w
        cv2.imshow('frame',img)
        cv2.waitKey(100) 
         


while y<=height:

    if x==0:
        right(x,y)
        y=y+h
        if cv2.waitKey(1) & 0xFF == 27:
            break

