# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:13:25 2019

@author: Karan Singh
"""

import math
def mean(numbers):
	return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

numbers = [1,2,3,4,5]
print('Summary of {0}: mean={1}, stdev={2}'.format(numbers, mean(numbers), stdev(numbers)))