# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:19:18 2019

@author: Karan Singh
"""

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)

print("Order Array is:")
print(a)
print("\n")

for x in np.nditer(a, op_flags = ['readwrite']):
    x[...] = 2*x

print("Modified Array Is:")
print (a)
