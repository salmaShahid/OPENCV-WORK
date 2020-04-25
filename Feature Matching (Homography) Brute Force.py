import numpy as np
import cv2
import matplotlib.pyplot as plt

#we're going to use a form of "brute force" matching. We're going to find all features in both images.
# Then we match these features. We then can draw out as many as we want.
# Careful though. If you draw say 500 matches, you're going to have a lot of false positives
img1 = cv2.imread(r'C:\Users\LeNoVo T430\PycharmProjects\MlLib\OpenCV\pic.jpEg',0)
img2 = cv2.imread(r'C:\Users\LeNoVo T430\PycharmProjects\MlLib\OpenCV\aaa.jpEg',0)
#So far we've imported the modules we're going to use, and defined our two images,
# the template (img1) and the image we're going to search for the template in (img2).
orb = cv2.ORB_create()
#This is the detector we're going to use for the features.
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

#Here, we find the key points and their descriptors with the orb detector.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#This is our BFMatcher object.
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

#Here we create matches of the descriptors, then we sort them based on their distances.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
plt.imshow(img3)
plt.show()

