import requests

response = requests.get('https://api.covid19api.com/summary')

data = response.json()

for i in sorted(data):
     keyValues = data[i]
     print(keyValues)
