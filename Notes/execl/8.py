# importing xlwt module 
import xlwt 
  
workbook = xlwt.Workbook()  
  
sheet = workbook.add_sheet("Sheet Name") 
  
# Specifying style 
style = xlwt.easyxf('font: bold 1') 
  
# Specifying column 
sheet.write(0, 0, 'SAMPLE', style) 
workbook.save("sample.xls") 
