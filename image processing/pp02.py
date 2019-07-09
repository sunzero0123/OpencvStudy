import cv2

imageFile = 'C:/0710pcv/cof.png'
img = cv2.imread(imageFile)
cv2.imwrite('C:/0710pcv/cof.bmp',img)
cv2.imwrite('C:/0710pcv/cof.png',img)
cv2.imwrite('C:/0710pcv/cof.png',img,[cv2.IMWRITE_PNG_COMPRESSION,9])#압축률
cv2.imwrite('C:/0710pcv/cof.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,90])#품질범위