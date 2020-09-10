import requests

with open('path', 'r') as f:
    api_key = f.read

params = {
    'key': api_key,
    'lat': '40.027',
    'lon': '-105.2519'
}
endpoint = 'get-trails'

site = 'https://mtbproject.com/data/'

url = site + endpoint

response = requests.get(url, params=params)

print(response.json())