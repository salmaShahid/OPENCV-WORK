import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\LeNoVo T430\PycharmProjects\MlLib\OpenCV\pic.jpEg')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (90,35,250,250)

#we load in the image, create a mask, specify the background and foreground model,
# which is used by the algorithm internally.
# The real important part is the rect we define. This is rect = (start_x, start_y, width, height).

#the rectangle that encases our main object. If i'm using my image,
# that is the rect to use. If i use my own, find the proper coordinates for my image
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
#cv2.grabCut, which took quite a few parameters. First the input image,
# then the mask, then the rectangle for our main object, the background
# model, foreground model,
# the amount of iterations to run, and what mode you are using.
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
#the mask is changed so that all 0 and 2 pixels are converted to
# the background, where the 1 and 3 pixels are now the foreground.
# From here, we multiply with the input image.
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()