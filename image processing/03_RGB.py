import cv2
from matplotlib import pyplot as plt

imageFile = 'C:/0710pcv/cof.png'
imgBGR = cv2.imread(imageFile)#opencv->BGR
plt.axis('off')#x축,y축 표시를 하지 않는다
#plt.imshow(imgBGR)
#plt.show()

imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)#matplot->RGB
plt.imshow(imgRGB)
plt.show()