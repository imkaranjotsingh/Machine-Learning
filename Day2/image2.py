import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(1,2,1),plt.imshow(img,cmap = 'Greens')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(edges,cmap = 'Greens')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
