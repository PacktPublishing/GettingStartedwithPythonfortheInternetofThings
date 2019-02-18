import sys
import cv2
import numpy as np

# Load input image
in_file = sys.argv[1]
image = cv2.imread(in_file)

# Convert it to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Input grayscale image', image_gray)

# Equalize the histogram
image_gray_histoeq = cv2.equalizeHist(image_gray)
cv2.imshow('Histogram equalized - grayscale image', image_gray_histoeq)

# Histogram equalization of color images
image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

image_yuv[:,:,0] = cv2.equalizeHist(image_yuv[:,:,0])

image_histoeq = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Input image', image)
cv2.imshow('Histogram equalized - color image', image_histoeq)
cv2.waitKey()
