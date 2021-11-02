import requests 
import json 

r = requests.get('http://localhost:3000')
data = r.json()

print(data)