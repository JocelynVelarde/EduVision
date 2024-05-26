import cv2
from deepface import DeepFace
import numpy as np


# Load the pre-trained SSD model and the prototxt file
face_detector = cv2.dnn.readNetFromCaffe(
    'deploy.prototxt.txt',
    'res10_300x300_ssd_iter_140000.caffemodel'
)

# Initialize the video capture
cap = cv2.VideoCapture(0)

emotion_counts = {
    'happy': 0,
    'sad': 0,
    'angry': 0,
    'surprise': 0,
    'fear': 0,
    'neutral': 0,
    'disgust': 0
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Prepare the frame for the face detector
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    face_detector.setInput(blob)
    detections = face_detector.forward()

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
            if emotion in emotion_counts:
                emotion_counts[emotion] += 1

            # Draw rectangle around face and label with predicted emotion
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 0, 255), 2)
            cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            # Draw "T" on the face
            # Vertical line
            cv2.line(frame, ((x + x1) // 2, y), ((x + x1) // 2, y1), (0, 255, 0), 2)
            # Horizontal line
            cv2.line(frame, (x, (y + y1) // 2), (x1, (y + y1) // 2), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Real-time Emotion Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(emotion_counts)
        break

cap.release()
cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()




"""
{
'emotion': {'angry': 18.126073479652405, 
             'disgust': 0.0254500366281718, 
             'fear': 42.87395775318146, 
             'happy': 0.29395208694040775, 
             'sad': 21.102583408355713, 
             'surprise': 0.044106628047302365, 
             'neutral': 17.53387302160263}, 
'dominant_emotion': 'fear', 
'region': {'x': 14, 
           'y': 16, 
           'w': 212, 
           'h': 212, 
           'left_eye': (166, 93), 
           'right_eye': (81, 88)}, 
'face_confidence': 0.96}
"""