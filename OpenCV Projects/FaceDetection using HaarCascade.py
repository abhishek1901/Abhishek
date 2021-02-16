import cv2
import numpy as np

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect(frame):

    face_rect = face_cascade.detectMultiScale(frame,1.64,5)

    for (x,y,width,height) in face_rect:
        
        cv2.rectangle(frame,(x,y),(x+width,y+height),(255,255,255),10)
        cv2.putText(frame,'  FACE',(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),1)


    return frame


while True:
     ret,frame = cap.read()

     frame = detect(frame)

     cv2.imshow('frame',frame)

     if cv2.waitKey(1) & 0xFF == ord('q'):
         break



