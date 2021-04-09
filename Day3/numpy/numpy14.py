# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:05:48 2019

@author: Karan Singh
"""

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)

print("First Array is:")
print(a)
print("\n")

print("Second Array is:")
b = np.array([1,2,3,4], dtype = int)
print(b)
print("\n")

print("Modified Array is:")
for x,y in np.nditer([a,b]):
    print("%d:%d"%(x,y))
z = 0
u = 0
for z,u in range([6,6]):
    print("%d:%d"%(z,u))