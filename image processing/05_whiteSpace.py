#matplotlib에서 여백제거
import cv2
from matplotlib import pyplot as plt

imageFile = 'C:/0710pcv/cof.png'
imgGray = cv2.imread(imageFile,cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(6,6))
plt.subplots_adjust(left = 0, right =1 , bottom = 0, top =1.3 )#left < right ,bottom < top.
plt.imshow(imgGray,cmap='gray')
#plt.axis('tight')
plt.axis('off')
plt.savefig('C:/0710pcv/0711.png')
plt.show()