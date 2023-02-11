import cv2
import numpy as np 

img = np.zeros((512,512,3),np.uint8)

img[:]=255,0,0
def shapes():
    cv2.line(img, (0,0), (512,512), (0,250,0),3)
    cv2.circle(img, (256,256), 20, (0,0,250),3)
    cv2.rectangle(img, (128,128),(384,384) , (0,0,250),3)
    cv2.imshow("Shape", img,)
    cv2.waitKey(0)
def text():
    cv2.putText(img, "Name", (230,256), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0),2)
    cv2.imshow("Text", img,)
    cv2.waitKey(0)

def combine():
    cv2.line(img, (0,0), (512,512), (0,250,0),3)
    cv2.circle(img, (256,256), 20, (0,0,250),3)
    cv2.rectangle(img, (128,128),(384,384) , (0,0,250),3)
    cv2.putText(img, "Name", (230,256), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0),2)
    cv2.imshow("Combine", img,)
    cv2.waitKey(0)

#shapes()
#text()
#combine()
