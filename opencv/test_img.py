import numpy as np

import cv2

IMAGE_NAME='test.jpg'

#load image as grayscale
img = cv2.imread(IMAGE_NAME, 0)

img = cv2.resize(img,(400, 400))
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
