#importing necessary libraries
import cv2
import numpy as np

#reading the video
cap=cv2.VideoCapture("input.mp4")

#taking the upper and lower range for green colour
lower_range=np.array([30, 40, 60])
upper_range=np.array([89, 255, 255])

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))

    #from BGR to HSV 
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Creating Mask
    mask=cv2.inRange(hsv,lower_range,upper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    #Finding the contour
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #for tracking of green colour balls
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            x1 = int(x+x+w)//2
            y1 = int(y+y+h)//2
            cv2.circle(frame, (x1,y1), 4, (0,0,255), -1)
            
    cv2.imshow("FRAME",frame)
    cv2.imshow("FRAME1",mask)
    key = cv2.waitKey(0) & 0xFF
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()