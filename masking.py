import cv2 as cv
import numpy as np

img = cv.imread('Pics\Shiba.jpg')
cv.imshow('Shiba', img)
blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2-60,img.shape[0]//2-50), 50, 255, -1)
cv.imshow('Mask', mask)

masked_image = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked image', masked_image)
cv.waitKey(0)