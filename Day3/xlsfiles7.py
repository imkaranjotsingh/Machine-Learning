# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:11:42 2019

@author: Karan Singh
"""

# importing xlwt module 
import xlwt 
  
workbook = xlwt.Workbook()  
  
sheet = workbook.add_sheet("Book1.xlsx") 
  
# Specifying style 
style = xlwt.easyxf('font: bold 1') 
  
# Specifying column 
sheet.write(0, 0, 'SAMPLE', style) 
workbook.save("sample.xls") 
