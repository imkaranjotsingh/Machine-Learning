# importing xlwt module 
import xlwt 
  
workbook = xlwt.Workbook()  
  
sheet = workbook.add_sheet("Sheet Name") 
  
# Applying multiple styles 
style = xlwt.easyxf('font: bold 1, color red;') 
  
# Writting on specified sheet 
sheet.write(0, 0, 'SAMPLE', style) 
  
workbook.save("sample.xls")
