import requests

city = input("도시 이름을 작성하세요. :")
api_key = "3a6f80e289e1493a5d11e6216a1cafbf"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
weather_data = response.json()

print(weather_data)