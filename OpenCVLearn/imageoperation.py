import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) # returns tuple rows, columns, and channels
print(img.size)  # Returns total number of pixels
print(img. dtype)  # Returns image datatype
b, g, r = cv2.split(img) # Splits up image into 3 channels

img = cv2.merge((b ,g ,r))  # Gives back image

ball = img[280:340, 330:390]    # Numpy index to obtain ball

img[273:333, 100:160] = ball

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

#dst = cv2.add(img2, img)
dst = cv2.addWeighted(img, .9, img2, .1, 0)


cv2.imshow('Image', img)
cv2.imshow('Image2', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()