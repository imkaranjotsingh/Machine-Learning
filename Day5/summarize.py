# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:15:45 2019

@author: Karan Singh
"""

def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries

dataset = [[1,20,0], [2,21,1], [3,22,0]]
summary = summarize(dataset)
print('Attribute summaries: {0}'.format(summary))