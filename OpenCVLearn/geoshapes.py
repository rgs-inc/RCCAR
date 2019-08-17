import numpy as np
import cv2

# To use existing image uncomment below:
# img = cv2.imread('lena.jpg', 1)

# Else to use numpy to create own image:

img = np.zeros([512, 512, 3], np.uint8)

# Params: source, startpoint, endpoint, BGR, thickness

img = cv2.line(img, (0,0), (255, 255), (0, 255, 0), 5)

img = cv2.arrowedLine(img, (0,255), (255, 255), (255, 0, 0), 5)

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 3)

# Note, if change thickness to -1 it will fill shape with color param

img = cv2.circle(img, (447, 63), 63, (100, 200, 45), -1)


font = cv2.FONT_ITALIC
img = cv2.putText(img, 'OpenCV', (10, 500), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()