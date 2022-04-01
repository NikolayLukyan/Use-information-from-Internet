import requests
import time
import json
def get_data(service, appid,city):
    while True:
        time.sleep(1)
        url = f'{service}?q={city}&appid={appid}'
        response = requests.get(url)
        if response.status_code == 200:
            print(url)
            break
    return response.json()

appid = 'b1b15e88fa797225412429c1c50c122a1'
service = 'http://samples.openweathermap.org/data/2.5/forecast/daily'
city = 'Altstadt'
response = get_data(service, appid, city)

print('Получен результат')
print(response)

with open('1_3_weather.json', 'w') as f:
    json_repo = json.dump(response, f)