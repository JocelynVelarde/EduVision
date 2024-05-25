import cv2 
import numpy as np

w,h = 360,200
fbRange = [6200,6800]



def findFace (img):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2,8)
    myFaceListC = []
    myFaceListArea = []
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cx = x+w //2
        cy = y+h //2
        area = w*h
        cv2.circle(img,(cx,cy),5,(0,255,0),cv2.FILLED)
        myFaceListC.append([cx,cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i],myFaceListArea[i]]
    else:
        return img, [[0,0],0]
    
if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    while True:
        p,img = cap.read()
        img = cv2.resize(img,(w,h))
        img, info = findFace(img)
        print("Area",info[1],"Center")
        cv2.imshow("Output",img)
        keyCode = cv2.waitKey(1)
        if cv2.getWindowProperty("Output", cv2.WND_PROP_VISIBLE) <1:
            break
    cv2.destroyAllWindows()