import cv2
import numpy as np
#
#VideoCapture(0) mention that, you are going to read from primary camera of the System 
#it can be 1 or other based on number of camera connected to System 

cap=cv2.VideoCapture(0)

#if it is successfully linked with camera
#isOpened() funtion will return True otherwise False

while cap.isOpened():

    #read function will return two parameters, res and img
    _,img=cap.read()
    cv2.imshow("Camera",img)

    #if you are using 64 bit machine then add & 0xFF along with if condition
    k=cv2.waitKey(10)
    if k == 27:
        break
 
#releasing the resources that used so far

cv2.destroyAllWindows()
cap.release()