import cv2

cap = cv2.VideoCapture(0)

counter = 0

while True:
    x,frame = cap.read()

    counter +=1

    flip = cv2.flip(frame,1)

    if counter % 2 == 0:
        cv2.imshow('Image',frame)
    else:
        cv2.imshow('Image',flip)

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break
