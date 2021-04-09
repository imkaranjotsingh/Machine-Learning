# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:56:34 2019

@author: Karan Singh
"""

import numpy as np

x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])

print("our Array is:")
print(x)
print("\n")

z = x[1:4,1:3]

print("After Slicing , Our Array Becomes:")
print(z)
print("\n")
 
y = x[1:4,[1,2]]

print("Slicing using advance index for coloumn:")
print(y)




 