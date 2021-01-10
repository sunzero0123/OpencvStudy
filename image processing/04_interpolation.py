import cv2
from matplotlib import pyplot as plt

imageFile = 'C:/0710pcv/cof.png'
imgGray = cv2.imread(imageFile,cv2.IMREAD_GRAYSCALE)
plt.axis('off')

plt.imshow(imgGray,cmap="gray",interpolation = 'bicubic')#cmap->colormap
plt.show()
#영상의 Resize시 확대,축소로 인해 이미지에 대한 보간법(interpolation)이 요구된다
#확대와 축소로 인한 이미지의 소실 및 블록화 등의 문제가 발생