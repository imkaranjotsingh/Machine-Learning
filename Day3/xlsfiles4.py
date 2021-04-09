# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:52:00 2019

@author: Karan Singh
"""

# Program extracting first column 
import xlrd 
  
loc = ("Book1.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
  
for i in range(sheet.nrows): 
    print(sheet.cell_value(i, 0))