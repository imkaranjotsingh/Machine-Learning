# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:46:37 2019

@author: Karan Singh
"""

# Program extracting all columns 
# name in Python 
import xlrd 
  
loc = ("Book1.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0) 
  
for i in range(sheet.ncols): 
    print(sheet.cell_value(0, i)) 