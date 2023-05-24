import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Image
img = cv.imread('Pics\Kittens.jpg')
cv.imshow('img', img)

# Gray img
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey img', gray)

# Masking
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 50, 255, -1)
cv.imshow('Mask', circle)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Masked image', mask)

# Grayscale Histogram
# [0] channel index. Grayscale only has one channel, so we calculate that one. 
# [256] number of bins. Each bin represents a range of intesity values
# [0, 256] range of bins to be considered. Grayscale typically have intensity values 0-255. 
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# Mask Histogram
# Using gray in combination with masked_image allows to calculate a histogram incorporating the full range of intensities withing the masked region.
# a more comprehensive analysis

gray_masked_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

# Plotting the histogram
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_masked_hist)
plt.xlim([0,256])
plt.show()


cv.waitKey(0)
