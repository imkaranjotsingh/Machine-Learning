# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:43:29 2019

@author: Karan Singh
"""

import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
# Check the versions of libraries

# Python version
import sys

year = [1960, 1970, 1980, 1990, 2000, 2010]
pop_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]
pop_england = [100.23, 300.36, 689.86, 400.54,400.55,300.26]
plt.plot(year, pop_pakistan, color='green')
plt.plot(year, pop_england,color = 'red')
plt.plot(year, pop_india, color='orange')
plt.xlabel('Countries')
plt.ylabel('Population in million')
plt.title('Pakistan India Population till 2010')
plt.show()



