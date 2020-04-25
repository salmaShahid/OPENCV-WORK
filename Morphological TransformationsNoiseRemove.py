#for remove noise from filter
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8) #numpy ones with datatype its a slider
    #Erosion is where we will "erode" the edges. The way these work is we work with a slider (kernel).
    # We give the slider a size, let's say 5 x 5 pixels. What happens is we slide this slider around,
    # and if all of the pixels are white,
    #  then we get white, otherwise black. This may help eliminate some white noise
    erosion = cv2.erode(mask, kernel, iterations=1)
    #Dilation, which basically does the opposite: Slides around,
    # if the entire area isn't black, then it is converted to white
    dilation = cv2.dilate(mask, kernel, iterations=1)
    #The goal with opening is to remove "false positives" so to speak.
    #  Sometimes, in the background, we get some pixels here and there of "noise."
    # The idea of "closing" is to remove false negatives. Basically this is where we
    # have our detected shape, like our hat,
    # and yet we still have some black pixels within the object.
    # Closing will attempt to clear that up.
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


    #Two other options that aren't really useful for our case here are "tophat" and "blackhat:"

    # It is the difference between input image and Opening of the image
    # cv2.imshow('Tophat',tophat)

    # It is the difference between the closing of the input image and input image.
    # cv2.imshow('Blackhat',blackhat)
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()