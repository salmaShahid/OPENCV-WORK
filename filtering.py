import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #"Hue Saturation Value." This can help you actually pinpoint a more specific color,
    # based on hue and saturation ranges, with a variance of value

    lower_red = np.array([30, 150, 50]) #depend on your choice
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF #escape key
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()