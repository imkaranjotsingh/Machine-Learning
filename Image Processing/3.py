import matplotlib.pyplot as plt
img=plt.imread('sword.png')
print(img[:3])
plt.axis("off")
imgplot = plt.imshow(img)
lum_img = img[:,:,1]
#print(lum_img)
plt.axis("off")
imgplot = plt.imshow(lum_img)
 

