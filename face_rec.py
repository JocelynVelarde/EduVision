import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

# Initialize emotion counts
emotion_counts = {
    'happy': 0,
    'sad': 0,
    'angry': 0,
    'surprise': 0,
    'fear': 0,
    'neutral': 0,
    'disgust': 0
}

frame_count = 0
process_every_n_frames = 1

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)


    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    #emotion_list = []
    for (x, y, w, h) in faces:
        face_roi = rgb_frame[y:y + h, x:x + w]
        # Perform emotion analysis on the face ROI
        result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
        print(result[0])
        # Determine the dominant emotion
        emotion = result[0]['dominant_emotion']

        #emotion_list.append(emotion)
        # Update the count for the detected emotion
        #if emotion in emotion_counts:
        #    emotion_counts[emotion] += 1
        # Draw rectangle around face and label with predicted emotion
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    
    #print(emotion_list)

    # Display the resulting frame
    cv2.imshow('Real-time Emotion Detection', frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #print(emotion_counts)
        break


cap.release()
cv2.destroyAllWindows()