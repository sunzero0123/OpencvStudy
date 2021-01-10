import cv2

videoFile1 = 'C:/0710pcv/test.mp4'
cap = cv2.VideoCapture(videoFile1)

while True:
    if(cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT)):
        cap.open(videoFile1)

    ret, frame = cap.read()
    cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(33) > 0:
        break

cap.release()
cv2.destroyAllWindows()