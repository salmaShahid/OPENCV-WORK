import cv2
import numpy as np
cap = cv2.VideoCapture(0) #web cam 0

fourcur = cv2.VideoWriter_fourcc(*'XVID') #save video (4-byte code used to specify the video codec.)
out = cv2.VideoWriter('output.avi', fourcur, 20.0, (640,480)) #save video
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert color frame to gray
    cv2.imshow('frame', frame)
    cv2.imshow('gray',gray)
    out.write(frame) #save color video
    if cv2.waitKey(1) & 0xFF == ord('q'): #press q key
        break #break from loop

cap.release()
out.release() #reelase it after saving
cv2.destroyAllWindows()


