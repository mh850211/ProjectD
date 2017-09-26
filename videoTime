import numpy as np
import cv2
import datetime
import time
cap = cv2.VideoCapture(0)
a='/home/pi/videoRecord/'
b=time.strftime("%Y_%m_%d_%H %M")
c='.mp4'
now = datetime.datetime.now()
beftime=now.minute
cap.set(3,320)
cap.set(4,240)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter(a+b+c, fourcc, 20, (320,240))
while(cap.isOpened()):
    ret, frame = cap.read()
    now = datetime.datetime.now()
    sudo print ("sda")
    afttime=now.minute
    print (afttime-beftime)
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if afttime-beftime > 1:
            out.release()
            b=time.strftime("%Y_%m_%d_%H %M")
            beftime=now.minute
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
