import cv2

# To read:
#   First parameter is image name
#   Second parameter is how to: 1 color image 0 greyscale -1 as is

img = cv2.imread('lena.jpg', -1)

# print(img) Use this to test if filepath is correct

# To show image:

cv2.imshow('Image Sample', img)
k = cv2.waitKey(0) & 0xFF  # Wait-key 0 is infinite time

if k == 27:
    cv2.destroyAllWindows()

# To write an image in form of a file

elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()
