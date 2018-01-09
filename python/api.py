import requests
payload = {'APPID': '9ef3311b380d2586bf47ff522529e7a9',
          'q': 'portland'}
r = requests.post('https://api.openweathermap.org/data/2.5/weather', params=payload)
data = r.json()
temp = data['main']['temp'] * (9/5) - 459.67
print(r.url)
