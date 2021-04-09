# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:11:08 2019

@author: Karan Singh
"""

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)

print("Original Array is:")
print(a)
print("\n")

print("Sorted in C-style order:")
for x in np.nditer(a,order = 'C'):
    print(x)
print("\n")

print("Sorted in F-Style order:")
for x in np.nditer(a, order = 'F'):
    print(x)

