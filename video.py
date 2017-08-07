import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)
a='/home/pi/videoRecord/'
b=time.strftime("%Y-%m-%d-%H:%M")
c='.mp4'
cap.set(3,320)
cap.set(4,240)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter(a+b+c, fourcc, 20, (320,240))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
