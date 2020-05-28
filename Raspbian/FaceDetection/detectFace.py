import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('./Raspbian/FaceDetection/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 640) # 넓이 설정
cap.set(4, 480) # 높이 설정

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1) # 상하반전 -1 좌우반전 0 정상 1 상하좌우반전 2
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray, 
        scaleFactor = 1.2, 
        minNeighbors = 5, 
        minSize = (20, 20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('img', img) # img라는 이름으로 출력
    #cv2.imshow('gray', gray)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()