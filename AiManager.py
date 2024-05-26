import cv2
class AiManager:

    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        print("sdf")

    def findFace(self, img):

        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = self.faceCascade.detectMultiScale(imgGray, 1.2, 8)

        myFaceListC = []
        myFaceListArea = []

        bboxes = []

        for (x, y, w, h) in faces:

            bboxes.append((x, y, w, h))

            cx = x + w // 2
            cy = y + h // 2
            area = w * h

            #cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
            #myFaceListC.append([cx, cy])
            #myFaceListArea.append(area)

        return bboxes


