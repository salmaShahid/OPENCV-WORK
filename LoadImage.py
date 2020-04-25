#intro and load images
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\LeNoVo T430\PycharmProjects\MlLib\OpenCV\pic.jpEg',cv2.IMREAD_GRAYSCALE) #convert in gray
#IMREAD_COLOR 0(gray) 1 (color)
#IMREASD_UNCHANGED (-1)
# print(img.shape)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('mypicInGray.png',img) #to save an image
# #with plot help
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50,100],[80,100], 'c', linewidth = 5) #c is for color
# plt.show()