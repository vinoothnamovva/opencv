import cv2 as cv
import numpy as np
import os

#Read an image
img_color = cv.imread('test.jpg', 1) #color
img_grayscale = cv.imread('test.jpg', 0) #b&w
img_unchanged = cv.imread('test.jpg', -1) #unchanged

#Display an image
cv.imshow('Coloured Image', img_color)
cv.imshow('Black&White Image', img_grayscale)
cv.imshow('Unchanged Image', img_unchanged)

#Genereted windows wait indefinetly for keystroke
cv.waitKey(0)

#Destroy all generated windows
cv.destroyAllWindows()


#Write an image
cv.imwrite(r'C:\Users\vinoo\OneDrive\Documents\Image\grayscale.jpg', img_grayscale)

image_path = r'C:\Users\vinoo\OneDrive\Documents\Image\grayscale.jpg'

if os.path.exists(image_path):
    print("Image saved successfully..")
else:
    print("Image saving failed..")