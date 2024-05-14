# 890ff22657fabbb6e7bfbc1d0359bbd9

import requests
from datetime import datetime
coords = (59.9386, 30.3141)
API_KEY = '890ff22657fabbb6e7bfbc1d0359bbd9'
url = 'https://api.openweathermap.org/data/2.5/weather?'
params = {
    'lat': coords[0],
    'lon': coords[1],
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'ru'
}

response = requests.get(url, params=params)
data = response.json()
print(data)

main = data['main']
description = data['weather'][0]['description']
wind = data['wind']
sunrise = data['sys']['sunrise']
sunset = data['sys']['sunset']
print(f"Температура {main['temp']} C, {description}")
# print(data['weather'])
print(f"Ощущается как {main['feels_like']} C")
print(f"Ветер {wind['speed']} м/с")
print(f"Влажность {main['humidity']}%")
print(f"Восход в {datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')}")
print(f"Закат в {datetime.fromtimestamp(sunset).strftime('%H:%M:%S')}")





