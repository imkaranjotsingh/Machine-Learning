Openpyxl is a Python library for reading and writing Excel (with extension xlsx/xlsm/xltx/xltm) files. The openpyxl module allows Python program to read and modify Excel files.

For example, user might have to go through thousands of rows and pick out few handful information to make small changes based on some criteria. Using Openpyxl module, these tasks can be done very efficiently and easily.

Use this command to install openpyxl module :

sudo pip3 install openpyxl 
-----------------
# Python program to read an excel file 
  
# import openpyxl module 
import openpyxl 
  
# Give the location of the file 
path = "C:\\Users\\Admin\\Desktop\\demo.xlsx"
  
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