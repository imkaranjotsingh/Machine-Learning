# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:28:41 2019

@author: Karan Singh
"""

import operator
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response  = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key = operator.itemgetter(1),reverse = True)
    return sortedVotes[0][0]
neighbors = [[1,1,1,'a'],[2,2,'a'],[3,3,'b']]
print(getResponse(neighbors))