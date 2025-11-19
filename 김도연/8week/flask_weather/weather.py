import requests

city = input("Enter city name: ")
api_key = "bae1df25c37b890927e8ea8995414bac"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lon=10.99&appid={api_key}&units=metric"
# units=metric 섭씨, units=imperial 화씨

response = requests.get(url)
weather_data = response.json()

print(weather_data)