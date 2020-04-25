import numpy as np
import cv2

img = cv2.imread(r'C:\Users\LeNoVo T430\PycharmProjects\MlLib\OpenCV\pic.jpEg',cv2.IMREAD_COLOR)
# print(img.shape)
#line(start,end(depend on img), clor(blue -> 255,0,0 green-> 0,255,0 red-> 0,0,255 white-> 255,255,255 black->0,0,0)
cv2.line(img, (0,0), (545,545),(255,255,255), 15) #for line
cv2.rectangle(img, (55,95),(350,450),(0,255,0),3)#topleftcorner,botteomleftcorner, clor green, alignmrnt  #for rectangle
cv2.circle(img,(100,63),55,(0,0,255),-1) #center,radius,color(red), alignment
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
# pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'SalmaPic!',(0,130),font, 2,(200,255,255),5,cv2.LINE_AA)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

