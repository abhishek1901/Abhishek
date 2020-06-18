import cv2
import numpy as np

img = cv2.imread('Desktop\dog.jpeg')

print(img.shape)

cv2.line(img,(0,0),(1100,628),(255,0,0),5)

while True:
    cv2.imshow('frame',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



     