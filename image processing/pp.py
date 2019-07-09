import cv2
imageFile = 'C:/0710pcv/cof.png'
img = cv2.imread(imageFile)
img2 = cv2.imread(imageFile,0)
cv2.imshow('cof color',img)
cv2.imshow('cof graceScale',img2)
cv2.waitKey()#delay = 0
cv2.destroyAllWindows()