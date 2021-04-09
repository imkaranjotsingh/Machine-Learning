# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:24:16 2019

@author: Karan Singh
"""

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)

print("Original Array is:")
print(a)
print("\n")

print("Transpose of the original array is:")
b = a.T
print(b)
print("\n")

print("Modified array is:")
for x in np.nditer(b):
    print (x)
    
 