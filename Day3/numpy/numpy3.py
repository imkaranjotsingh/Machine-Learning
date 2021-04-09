# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:08:27 2019

@author: Karan Singh
"""

import numpy as np

x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])

print("our Array is:")
print(x)
print("\n")

print(x[ x > 5 ])