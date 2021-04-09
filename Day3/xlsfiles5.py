# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:57:24 2019

@author: Karan Singh
"""

# Program to extract a particular row value 
import xlrd 
  
loc = ("Book1.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
sheet.cell_value(0, 0) 
  
print(sheet.row_values(1)) 