import cv2 as cv
import numpy as np

#a blank image we can draw on
#uint8 is the datatype of an image
blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. Paint the image a certain color
# blank[100:150, 150:200] = 255,0,0
# cv.imshow('Blue Box', blank)

# 2. Draw a rectangle
# cv FILLED = -1
# blank.shape[0] bland.shape[1] = get size of width,height

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=-1)
# cv.imshow('Red Thick Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (250,250), 60, (0,255,0), thickness=2)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=2 )
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, "Rosebud...", (50,126), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)


