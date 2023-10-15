import requests
import json

API_KEY = '9b2759f59f2ad62897009ef9ff611551'
CITY = 'Almaty'

url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

response = requests.get(url)

# print(response.json())
if response.status_code == 200:
    data = response.json()
    print(f'City: {CITY}')
    print(f'Wather: {data["weather"][0]["description"]}')
    print(f'Температура: {data["main"]["temp"]} К')
    print(f'Страна: {data["sys"]["country"]}')
else:
    print('Error')
