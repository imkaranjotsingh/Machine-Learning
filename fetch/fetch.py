import requests
import os
'''
params = {
  'api_key': '{API_KEY}',
}
'''
r = requests.get('http://localhost:8181/sal')

with open('/tmp/movies.tmp.json', 'w') as f:
  f.write(r.text)

os.rename('/tmp/movies.tmp.json', '/tmp/movies.json')
