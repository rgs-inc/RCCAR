import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.imshow('Image', img)
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycolorImage = np.zeros((512,512,3), np.uint8)

        mycolorImage[:] = [blue, green, red]

        cv2.imshow('Color', mycolorImage)


img = cv2.imread('lena.jpg')
cv2.imshow('Image', img)

cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()