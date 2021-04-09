import scipy.misc
face = scipy.misc.face()
print(face.shape)
print(face.max)
print(face.dtype)
import matplotlib.pyplot as plt
#plt.axis("off")
plt.gray()
plt.imshow(face)
plt.show()
