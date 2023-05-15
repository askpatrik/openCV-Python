import cv2 as cv

img = cv.imread('Pics\Shiba.jpg')
cv.imshow('Dog', img)

cv.waitKey(0)