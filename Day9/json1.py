import requests
import  simplejson as json

# Goole Maps API.
link = 'http://maps.googleapis.com/maps/api/directions/json?origin=Chicago,IL&destination=Los+Angeles,CA&waypoints=Joplin,MO|Oklahoma+City,OK&sensor=false'

# Request data from link as 'str'
data = requests.get(link).text

# convert 'str' to Json
data = json.loads(data)
print(data);
# Now you can access Json 
