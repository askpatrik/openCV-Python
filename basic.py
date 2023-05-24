import cv2 as cv

img = cv.imread('Pics\Shiba.jpg')
cv.imshow('Shiba', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Shiba', gray)

color = cv.cvtColor(img, cv.COLOR_BGR2LUV)
cv.imshow('PurpleTint Shiba', color)

# Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT )
cv.imshow('Blurred Shiba', blur)

# Edge cascade
canny = cv.Canny(blur, 100, 150)
cv.imshow('Shiba Edges', canny)

# Dilating 
dilated = cv.dilate(canny, (7,7),iterations=3)
cv.imshow("Dilated Canny Shiba", dilated)

# Eroding 
eroded = cv.erode(dilated,(7,7), iterations=3)
cv.imshow("Eroded Canny Shiba", eroded)

# Resize
resize = cv.resize(img, (900,900), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized Shiba", resize)

#  Cropping
crop = resize[350:550, 550:700]
cv.imshow("Cropped Shiba", crop)

cv.waitKey(0)
