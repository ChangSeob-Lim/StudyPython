import cv2
import numpy as np
import os

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('./Raspbian/FaceDetection/trainer.yml') #
cascadePath = './Raspbian/FaceDetection/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

# names related to ids: example ==> hugo: id=1 etc
# 이런식으로 사용자의 이름을 사용자 수만큼 추가해준다.
names = ['None', 'Seob']

# 실시간 비디오 초기화
cam = cv2.VideoCapture(0)
cam.set(3,640) # 넓이 설정
cam.set(4,480) # 높이 설정

# 얼굴 인식을 위한 최소 윈도우 사이즈
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img = cam.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray, 
        scaleFactor = 1.2, 
        minNeighbors = 5, 
        minSize = (int(minW), int(minH))
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        id, confidence = recognizer.predict(gray[y:y+h, x:x+h])

        # Check if confidence is less them 100 ==> '0' is perfect match
        if confidence < 100:
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence)) # 이 아래에 제어로 로직 추가하면 됨
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x+5, y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5, y+h-5), font, 1, (255,255,0), 1)

    cv2.imshow('image', img) # img라는 이름으로 출력

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

#클린업
cam.release()
cv2.destroyAllWindows()