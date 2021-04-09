import requests
resp = requests.post('https://todolist.example.com/tasks/', json=task)
# The equivalent longer version
resp = requests.post('https://todolist.example.com/tasks/',
                     data=json.dumps(task),
                     headers={'Content-Type':'application/json'});