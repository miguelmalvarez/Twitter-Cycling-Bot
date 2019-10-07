import requests

## Test weather, then move to forecast
base_url = 'http://api.openweathermap.org/data/2.5/weather'
city = 'London,uk'

## Use config for this
appid = ''

request = base_url+'?q={}&{}'.format(city, appid)

res = requests.get(request)
data = res.json()

print(data)