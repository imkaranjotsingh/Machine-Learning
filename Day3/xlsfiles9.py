# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:25:23 2019

@author: Karan Singh
"""
# Python program to read an excel file 
  
# import openpyxl module 
import openpyxl 
  
# Give the location of the file 
path = "F:\Python Tution\Machine Learning\Day3\Book1.xlsx"
  
# To open the workbook  
# workbook object is created 
wb_obj = openpyxl.load_workbook(path) 
  
# Get workbook active sheet object 
# from the active attribute 
sheet_obj = wb_obj.active 
  
# Cell objects also have row, column,  
# and coordinate attributes that provide 
# location information for the cell. 
  
# Note: The first row or  
# column integer is 1, not 0. 
  
# Cell object is created by using  
# sheet object's cell() method. 
cell_obj = sheet_obj.cell(row = 1, column = 1) 
  
# Print value of cell object  
# using the value attribute 
print(cell_obj.value) 