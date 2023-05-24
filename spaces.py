import cv2 as cv

img = cv.imread('Pics\Shiba.jpg')

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)




cv.imshow('BGR Shiba', img)
cv.imshow('LAB Shiba', lab)
cv.imshow('LAB --> BGR Shiba', lab_bgr)

cv.waitKey(0)