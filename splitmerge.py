import cv2 as cv
import numpy as np 


img = cv.imread('Pics\Shiba.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')

# Split it
b,g,r = cv.split(img)

cv.imshow('image', img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

# Merge it
merged = cv.merge([b,g,r])
cv.imshow('merged shiba', merged)

# Visualize distribution by Merging with blanks
blue = cv.merge([b, blank, blank])
red = cv.merge([blank,blank,r])
green = cv.merge([blank,g, blank])

cv.imshow('blue Shiba', blue)
cv.imshow('red Shiba', red)
cv.imshow('green Shiba', green)

cv.waitKey(0)