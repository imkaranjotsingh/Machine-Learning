# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:25:50 2019

@author: Karan Singh
"""

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)

print("Original Array is:")
print(a)
print("\n")

for x in np.nditer(a):
    print(x)

print("Transpose of the Original Array is:")
b = a.T
print(b)
print("\n")

for x in np.nditer(b):
    print(x)
print("\n")

print("Sorting in C-Style order:")
c = b.copy(order = 'C')
print(c)
for x in np.nditer(c):
    print(x)
    
print("\n")

print("Sort in F-style Order:")
c = b.copy(order = 'F')
print(c)

for x in np.nditer(c):
    print(x)
    
