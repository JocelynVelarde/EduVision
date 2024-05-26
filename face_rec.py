import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
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

frame_count = 0

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)


    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    emotion_list = []
    for (x, y, w, h) in faces:
        face_roi = rgb_frame[y:y + h, x:x + w]
        # Perform emotion analysis on the face ROI
        result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
        # Determine the dominant emotion
        emotion = result[0]['dominant_emotion']
        if emotion in emotion_counts:
            emotion_counts[emotion] += 1


        # Draw rectangle around face and label with predicted emotion
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        # Draw "T" on the face
        # Vertical line
        cv2.line(frame, (x + w // 2, y), (x + w // 2, y + h), (0,255,0), 2)
        # Horizontal line
        cv2.line(frame, (x, y + h // 2), (x + w, y + h // 2),(0,255,0), 2)
    

    # Display the resulting frame
    cv2.imshow('Real-time Face Detection', frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(emotion_counts)
        break


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