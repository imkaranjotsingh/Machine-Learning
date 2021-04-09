# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:37:03 2019

@author: Karan Singh
"""


# Program to extract number of 
# columns in Python 
import xlrd 
  
loc = ("Book1.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0) 
  
# Extracting number of columns 
print(sheet.ncols) 