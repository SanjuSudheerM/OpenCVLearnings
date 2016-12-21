########################################
#
#   Hand Detection with Fingers
#   Developer: Sanju M 
#
########################################
import cv2
import numpy as np
firstFrame=None

cap=cv2.VideoCapture(0)
while cap.isOpened():
    _,img=cap.read()
    cv2.rectangle(img,(10,10),(300,300),(140,180,30),3)
    image=img[10:300,10:300]
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),1)
    if firstFrame is None:
		firstFrame = gray

    # diff=cv2.absdiff(firstFrame,gray)25
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow("Image11",thresh)
    contours,heirarchy=cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours)>0:
        count=0
        bigContour=contours[0]
        for i in contours:
            if cv2.contourArea(i)<41000 and cv2.contourArea(i)>500:
                # if cv2.contourArea(i)>cv2.contourArea(bigContour):
                #     bigContour=i
                # print count ,": ",cv2.contourArea(i)
                M=cv2.moments(i)
                if M['m00'] != 0:
                    cx=int(M['m10']/M['m00'])
                    cy=int(M['m01']/M['m00'])
                else:
                    cx=0
                    cy=0
                # cv2.drawContours(img,i,-1,(0,255,0),5)
                hull=cv2.convexHull(i,returnPoints=False)
                defects=cv2.convexityDefects(i,hull)

                #print "length of Hull",len(hull)

                for pts in range(defects.shape[0]):
                    s,e,f,d=defects[pts][0]
                    print s,e,d,f
                    start=tuple(i[s][0])
                    end=tuple(i[e][0])
                    far=tuple(i[f][0])
                    print "Start",start
                    cv2.line(image,start,end,[0,255,0],2)
                    cv2.circle(image,far,5,[0,0,255],-1) 
                                            
               
                (x, y, w, h)  = cv2.boundingRect(bigContour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img,str(count),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
                count+=1
    cv2.imshow("Image",img)
    cv2.imshow("Imaae",image)
    firstFrame=gray

    k=cv2.waitKey(10) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()

