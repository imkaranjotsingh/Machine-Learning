import cv2
import numpy as np

img = cv2.imread('1.jpg')

res = cv2.resize(img,None,fx=3, fy=3, interpolation = cv2.INTER_CUBIC)

#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
