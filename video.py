import cv2
#Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#To capture video from webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
#Read the Frame in img
    _, img = cap.read()
#Convert to GrayScale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#Draw the Rectangle around the face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#Display the output
    cv2.imshow('img', img)
#Quit if q pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()