# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:49:03 2019

@author: Karan Singh
"""
import numpy as np
x = np.array([[ 0 , 1 , 2 ],[3 , 4 , 5 ],[ 6 , 7 , 8 ],[ 9 , 10, 11]])
print("Our Array is:")
print(x)
print('\n')

row = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[row,cols]

print("The Corner Element Of This Array Are:")
print (y)