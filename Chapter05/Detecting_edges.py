import sys
import cv2
import numpy as np

in_file = sys.argv[1]
image = cv2.imread(in_file, cv2.IMREAD_GRAYSCALE)

horizontal_sobel = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

vertical_sobel = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

laplacian_img = cv2.Laplacian(image, cv2.CV_64F)

canny_img = cv2.Canny(image, 30, 200)

cv2.imshow('Original', image)
cv2.imshow('horizontal Sobel', horizontal_sobel)
cv2.imshow('vertical Sobel', vertical_sobel)
cv2.imshow('Laplacian image', laplacian_img)
cv2.imshow('Canny image', canny_img)

cv2.waitKey()

cv2.imshow('Original', imgage)
cv2.imshow('horizontal Sobel', horizontal_sobel)
cv2.imshow('vertical Sobel', vertical_sobel)
cv2.imshow('Laplacian image', laplacian_img)
cv2.imshow('Canny image', canny_img)

cv2.waitKey()
