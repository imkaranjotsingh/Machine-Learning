# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:16:48 2019

@author: Karan Singh
"""

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)

print("Original Array is:")
print(a)
print("\n")

print("Modified Array is:")
for x in np.nditer(a):
    print(x)


