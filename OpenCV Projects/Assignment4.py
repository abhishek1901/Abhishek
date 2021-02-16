import cv2
import time

cap = cv2.VideoCapture(0)

while True:
     a = time.time()
     
     b = int(a)

     while b % 5 == 0:
         
         while True:
             n = time.time()

             c = int(n)

             print(c)
    
             x,frame = cap.read()

             flip = cv2.flip(frame,-1)

             if c % 5 == 0:
                 cv2.imshow('frame',flip)
             else:
                 cv2.imshow('frame',frame)

             if cv2.waitKey(1000) & 0xFF == ord('q'):
                  break    
         if cv2.waitKey(1000)& 0xFF == ord('q'):
                  break
     if cv2.waitKey(1000) & 0xFF == ord('q'):
                  break          
                 
     
     

