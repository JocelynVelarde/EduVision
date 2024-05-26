import cv2
import numpy as np
import threading
import time
from deepface import DeepFace
from ThreadManager import ThreadManager
from AiManager import AiManager

#manager = ThreadManager()

aimanager = AiManager(5)



#w, h = 360, 200
#fbRange = [6200, 6800]


def process_frame(frame):
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    aimanager.face_detector.setInput(blob)
    detections = aimanager.face_detector.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x, y, x1, y1) = box.astype("int")
            face_roi = frame[y:y1, x:x1]

            # Perform emotion analysis on the face ROI
            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            # Determine the dominant emotion
            emotion = result[0]['dominant_emotion']
            print(emotion)
    # Código de deepface
    print("Processing frame in a separate thread")

def data_process(dic):


    # Código de deepface
    print("Processing data separate thread")
    print(dic)


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    frame_counter_haar = 0
    frame_counter_deep = 0

    #manager.start_threads()

    bboxes = None

    fo = 0
    dis = 0

    while True:

        p, img = cap.read()

        if not p:
            break

        frame_counter_haar += 1
        frame_counter_deep += 1



        #img = cv2.resize(img, (w, h))

        if frame_counter_haar == 5:

            bboxes, fo, dis = aimanager.findFace(img)
            frame_counter_haar = 0

        if frame_counter_deep == 20:
            threading.Thread(target=process_frame, args=(img.copy(),)).start()

            data = {"timestamp": int(time.time()), "focused": fo, "distracted": dis}

            threading.Thread(target=data_process, args=(data,)).start()

            frame_counter_deep = 0

        if bboxes is not None:
            for (x, y, w, h) in bboxes:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("Output", img)
        keyCode = cv2.waitKey(1)
        if cv2.getWindowProperty("Output", cv2.WND_PROP_VISIBLE) < 1:
            break

    #manager.wait_for_threads()
    cv2.destroyAllWindows()
