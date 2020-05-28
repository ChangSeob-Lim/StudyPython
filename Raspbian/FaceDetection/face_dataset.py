import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # 넓이 설정
cam.set(4, 480) # 높이 설정

Face_detector = cv2.CascadeClassifier('./Raspbian/FaceDetection/haarcascades/haarcascade_frontalface_default.xml')
# 얼굴에 대해서 번호를 입력
face_id = input('\n enter user id end press <return> ==> ')
print('\n [INFO] Initializing face capture. Look the camera and wait ...')
# 개인 샘플링 얼굴 카운트 초기화
count = 0

while True:
    ret, img = cam.read()
    img = cv2.flip(img, -1) # 상하반전 -1 좌우반전 0 정상 1 상하좌우반전 2
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = Face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
        # dataset 폴더에 캡쳐이미지 저장
        cv2.imwrite('./Raspbian/FaceDetection/dataset/User.' + str(face_id) + '.' + str(count) + '.jpg', gray[y:y+h, x:x+w])

    cv2.imshow('image', img) # img라는 이름으로 출력

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
    elif count>=30: # 얼굴 샘플 30개
        break

#클린업
print('\n [INFO] Exiting Program and Cleanup stuff')
cam.release()
cv2.destroyAllWindows()