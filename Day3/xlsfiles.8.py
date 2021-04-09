# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:23:53 2019

@author: Karan Singh
"""

# importing xlwt module 
import xlwt 
  
workbook = xlwt.Workbook()  
  
sheet = workbook.add_sheet("Book1.xlsx") 
  
# Applying multiple styles 
style = xlwt.easyxf('font: bold 1, color red;') 
  
# Writting on specified sheet 
sheet.write(0, 0, 'SAMPLE', style) 
  
workbook.save("sample.xls")
