import cv2 as cv
import numpy as np

img = cv.imread('Pics\Shiba.jpg')

# Translation
# shifts the image by x pixels horizontally and y pixels vertically, and then returns the shifted image.
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x  --> right
# y --> down

translated = translate(img, -100, 100)
cv.imshow('Translated Shiba', translated)


#  Rotation
#  Rotating by some angle. CV lets you specify rotation point (usually center)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width,height)

        return cv.warpAffine(img, rotMat, dimensions)
    

rotated = rotate(img, 45)    
cv.imshow("Rotated Shiba", rotated)


# Resizing> different inter when enlarging or not
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resized)

# Flipping
flipped = cv.flip(img, -1)
cv.imshow("flip shiba", flipped)


# Cropping
cropped = img[400:500, 200:300]
cv.imshow("Crop Shiba", cropped)
cv.waitKey(0)