import cv2 as cv
import numpy as np

img = cv.imread('Pics\Shiba.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (1,1), cv.BORDER_DEFAULT)

cv.imshow('blur', blur)
cv.imshow('gray shiba', gray)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

# Blurred Canny (recommended)
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# Threshold (not recommended)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

# Find contours
contours, hierachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

# Draw contours on blank image
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('contours drawn', blank)

cv.waitKey(0)