# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:15:21 2019

@author: Karan Singh
"""
#In this example, NaN (Not a Number) elements are omitted by using ~ (complement operator).

import numpy as np
a = np.array([np.nan,1,2,np.nan,3,4,5])
print(a)
print(a[~np.isnan(a)])

