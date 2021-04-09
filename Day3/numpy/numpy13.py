# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:59:27 2019

@author: Karan Singh
"""

import numpy as np 
a = np.arange(0,60,5) 
a = a.reshape(3,4) 

print("Original Array is:")
print(a)
print("\n")

print("Modified Array is:")
for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
    print(x)
    