import requests 
import json 

print('Please enter your zip code: ')
zip = input() 

r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=%s&appid=0b021b11b88b46ea8d6b0a83a49c5ae7' % zip)
data = r.json()

#print(type(data['weather'][0]['description']))
print("The weather in %s is %s" % (zip, data['weather'][0]['description']))