import cv2

cap = cv2.VideoCapture(0)

n = int(input("Enter No. of frames"))

n=n+1

counter=0

def flipped(counter):
    if counter % n == 0:
        cv2.imshow('frame',flip)
    else:
        cv2.imshow('frame',frame)  


while True:
    x,frame = cap.read()

    flip = cv2.flip(frame,1)

    counter=counter+1
    flipped(counter)

    if cv2.waitKey(1000) & 0xFF == ord('a'):
        break

