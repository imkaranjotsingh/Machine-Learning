# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:20:15 2019

@author: Karan Singh
"""
#The following example shows how to filter out the non-complex elements from an array.
import numpy as np
a = np.array([1,2+6j,5,3.5+5j])
print(a[np.iscomplex(a)])
#print(a[~np.isnan(a)])