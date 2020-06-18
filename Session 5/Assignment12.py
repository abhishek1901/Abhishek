import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cornerpt1 = False
cornerpt2 = False

def crop(event,x,y,flags,param):

    global pts,cornerpt1,cornerpt2

    if event == cv2.EVENT_LBUTTONDOWN:

        if cornerpt1 == False:
            pts = [(x,y)]
            cornerpt1 = True
        elif cornerpt2 == False:
            pts.append((x,y))
            cornerpt2=True
        if len(pts) == 2:
            y1,y2,x1,x2 = pts[0][1],pts[1][1],pts[0][0],pts[1][0]
            cropped = frame[y1:y2,x1:x2]
            crop_gray = cv2.cvtColor(cropped,cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame1',crop_gray)
            cv2.imwrite('template.jpg',crop_gray)
            
            

cv2.namedWindow('frame')

cv2.setMouseCallback('frame',crop)

while True:
    ret,frame = cap.read()

    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if cornerpt1 == True and cornerpt2 == True:
        template = cv2.imread('template.jpg')
        w = template.shape[1]
        h = template.shape[0]
        res = cv2.matchTemplate(frame,template,cv2.TM_CCOEFF_NORMED)

        loc = np.where(res>0.85)

        for c,d in zip(*loc[::-1]):
            
            cv2.rectangle(frame,(c,d),(c+w,d+h),(255,255,255),1)
            cv2.putText(frame,'          HUMAN',(c,d),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1)
            
                

    cv2.imshow('frame',frame,)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break