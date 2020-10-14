import numpy as np
import cv2

img = cv2.imread('/home/pi/Pictures/img.jpeg')
img = cv2.resize(img,(400, 400))
cv2.imwrite("new_img.jpeg", img)
height, width, chnl = img.shape
print (height)
print (width)
print (chnl)

i = 0
j = 0
f = open("clr.txt", "a")
for i in range (height):
    for j in range (width):
        clr = img[i, j]
        f.write("Color at pixel [" + str(i) + " - " + str(j) +" ] : " + str(clr) +  "\n")

f.close()
