import cv2 as cv

img = cv.imread('Pics\Shiba.jpg')
cv.imshow('Shiba', img)

# Averaging
average = cv.blur(img, (5,5))
cv.imshow('Avg', average)

# Gaussian blue
gauss = cv.GaussianBlur(img, (3,3), 3)
cv.imshow('Gauss', gauss)

# Median blue
median = cv.medianBlur(img, 5)
cv.imshow('Median', median)

# BIlateral blur
bilateral = cv.bilateralFilter(img, 5, 5, 10)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)