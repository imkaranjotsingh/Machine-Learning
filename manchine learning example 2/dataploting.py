import requests
import simplejson as json
import matplotlib.pyplot as plt 

url = 'http://localhost:8181/sal'

print(url)
resp  = requests.get(url = url)
todos = json.loads(resp.text)
'''
name = []
salary = []
name.append(todos[0])
salary.append(todos[1])
'''
plt.plot(todos[0],todos[1])
plt.xlabel('Employee Name')
plt.ylabel('Salary')
plt.title('Salary OF Empoyees!!!!!') 
plt.show()
