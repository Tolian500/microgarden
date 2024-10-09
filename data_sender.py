import urequests
import requests
import json

url = 'http://37.27.94.203:5000/add_data'

data = {
    'temp': 0.01,
    'hum': 0.01
}

response = requests.get(url, json=data)
# response = urequests.post(url, json=data)
print(response.text)