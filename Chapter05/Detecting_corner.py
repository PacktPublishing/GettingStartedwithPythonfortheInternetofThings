import sys
import cv2
import numpy as np

# Load input image

in_file = sys.argv[1]
image = cv2.imread(in_file)
cv2.imshow('Input image', image)

image_gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray2 = np.float32(image_gray1)

# Harris corner detector
image_harris1 = cv2.cornerHarris(image_gray2, 7, 5, 0.04)

# Resultant image is dilated to mark the corners
image_harris2 = cv2.dilate(image_harris1, None)

# Threshold the image
image[image_harris2 > 0.01 * image_harris2.max()] = [0, 0, 0]

cv2.imshow('Harris Corners', image)
cv2.waitKey()
