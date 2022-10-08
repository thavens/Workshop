import requests

r = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=37.3229978&lon=-122.0321823&appid=eb2cd91b8f1ff010fdca630bbcd830cb')
print(r)
print(r.text)

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'lat': 37.3229978,
    'lon': -122.0321823,
    'appid': 'eb2cd91b8f1ff010fdca630bbcd830cb'
}
r = requests.get(url, params=params)
print(r)
print(r.text)
