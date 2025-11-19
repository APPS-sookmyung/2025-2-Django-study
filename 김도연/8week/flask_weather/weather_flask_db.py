from flask import Flask, render_template, request
import requests
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB 연결
client = MongoClient('mongodb://localhost:27017/')
db = client['weather_db']
collection = db['weather_collection']

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        city = request.form["city"]
        api_key = "bae1df25c37b890927e8ea8995414bac"  # 여기에 OpenWeatherMap API 키를 넣으세요.
        weather_data = get_weather(city, api_key)
        if weather_data["cod"] == 200:
            temperature = weather_data["main"]["temp"]
            feels_temp = weather_data["main"]["feels_like"]
            # MongoDB에 저장
            data = {"city": city, "temperature": temperature, "feels_temp": feels_temp}
            collection.insert_one(data)
            return render_template("result.html", city=city, temperature=temperature, feels_temp=feels_temp)
        else:
            error_message = "날씨 정보를 가져오는 중에 오류가 발생했습니다."
            return render_template("error.html", error_message=error_message)
    else:
        # MongoDB에서 데이터 검색
        weather_list = list(collection.find())
        return render_template("index.html", weather_list=weather_list)

if __name__ == "__main__":
    app.run(debug=True)