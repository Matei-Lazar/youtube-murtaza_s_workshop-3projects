# RESIZING AND CROPPING

import cv2
import numpy as np

img = cv2.imread("Resources/plane.jpg")
print(img.shape)

imgResize = cv2.resize(img,(1000, 500))

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image resize", imgResize)
cv2.imshow("Image cropped", imgCropped)

cv2.waitKey(0)