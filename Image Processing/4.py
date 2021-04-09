import numpy as np
import matplotlib.pyplot as plt
def tint(imag, percent):
    tinted_imag = imag + (np.ones(imag.shape) - imag) * percent
    return tinted_imag
windmills = plt.imread('a.png')
plt.imshow(windmills)
tinted_windmills = tint(windmills, 0.8)
#plt.axis("off")
plt.imshow(tinted_windmills)
plt.show()
