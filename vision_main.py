import cv2
import numpy as np
import threading

from ThreadManager import ThreadManager
from AiManager import AiManager

#manager = ThreadManager()

aimanager = AiManager()


w, h = 360, 200
fbRange = [6200, 6800]


def process_frame(frame):
    # Código de deepface
    print("Processing frame in a separate thread")


if __name__ == '__main__':

    cap = cv2.VideoCapture(1)

    frame_counter_haar = 0
    frame_counter_deep = 0

    manager.start_threads()

    while True:

        p, img = cap.read()

        if not p:
            break

        frame_counter_haar += 1
        frame_counter_deep += 1

        img = cv2.resize(img, (w, h))

        if frame_counter_haar == 5:

            img, info = aimanager.findFace(img)

            frame_counter_haar = 0

        if frame_counter_deep == 20:
            threading.Thread(target=process_frame, args=(img.copy(),)).start()
            frame_counter_deep = 0

        cv2.imshow("Output", img)
        keyCode = cv2.waitKey(1)
        if cv2.getWindowProperty("Output", cv2.WND_PROP_VISIBLE) < 1:
            break

    #manager.wait_for_threads()
    cv2.destroyAllWindows()
