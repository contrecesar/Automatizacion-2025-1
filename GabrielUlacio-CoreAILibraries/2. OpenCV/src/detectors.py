import cv2
import os

# Load the Haar Cascade model for face detection
face_cascade = cv2.CascadeClassifier(
    os.path.join('models', 'haarcascade_frontalface_default.xml')
)

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image
