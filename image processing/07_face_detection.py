import cv2


# Harr Cascade는 기계학습을 이용한 객체 탐지 알고리즘 

cascade_filename = 'C:/Users/asy10/opencvstudy/face_detection/face_detection/haarcascade_frontalface_alt.xml'

#모델 불러오기
face_cascade = cv2.CascadeClassifier(cascade_filename)

img =cv2.imread('C:/Users/asy10/opencvstudy/face_detection/face_detection/girl.jpg')

img = cv2.resize(img,(500,500))#image 크기 조절 
#Grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#얼굴 검출
faces = face_cascade.detectMultiScale(img_gray,1.1,3)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
    face = img[y: y+h, x: x+w]
    face_gray = img_gray[y: y+h, x: x+w]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

