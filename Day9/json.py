import requests
import xlsxwriter
import simplejson as json

url = 'http://api.androidhive.info/contacts/'

resp = requests.get(url=url)
data = json.loads(resp.text)
'''
id = []
name = []
email = []
address = []
gender = []
title = []
mobile = []
home = []
office = []
for x in todos.values():
    for y in x:
        for z,a in y.items():
            
            if z == 'id':
                id.append(a)
            elif z == 'name':
                name.append(a)
            elif z == 'email':
                email.append(a)
            elif z == 'address':
                address.append(a)
            elif z == 'gender':
                gender.append(a)
            elif z == 'phone':
                for w,t in a.items():
                    if w == 'mobile':
                        mobile.append(t)
                    if w == 'home':
                        home.append(t)
                    if w == 'office':
                        office.append(t)
            
                        
workbook = xlsxwriter.Workbook('contents.xlsx') 
worksheet = workbook.add_worksheet()
worksheet.write(0,0,'Id')
worksheet.write(0,1,'Name')
worksheet.write(0,2,'Email')
worksheet.write(0,3,'Address')
worksheet.write(0,4,'Gender')
worksheet.write(0,5,'Mobile No')
worksheet.write(0,6,'Home Phone no')
worksheet.write(0,7,'Office no')
row  = 1
column = 0
for item in id:
    worksheet.write(row, column , item)
    row += 1
row = 1
for item in name:
    worksheet.write(row, column + 1 , item)
    row += 1
row = 1
for item in email:
    worksheet.write(row, column + 2 , item)
    row += 1
row = 1
for item in address:
    worksheet.write(row, column + 3 , item)
    row += 1
row = 1
for item in gender:
    worksheet.write(row, column + 4 , item)
    row += 1
row = 1
for item in mobile:
    worksheet.write(row, column + 5 , item)
    row += 1
row = 1
for item in home:
    worksheet.write(row, column + 6 , item)
    row += 1
row = 1
for item in office:
    worksheet.write(row, column + 7 , item)
    row += 1

workbook.close()
'''
print(type(data['contacts']))
for a in data['contacts']: 
    print(a['id'])
    print(a['phone'])








