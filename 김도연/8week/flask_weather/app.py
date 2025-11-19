from flask import Flask, render_template, request
import requests
import folium

#folium: 지도 위치정보를 시각화하는 라이브러리

app = Flask(__name__)

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        city = request.form["city"]
        api_key = "bae1df25c37b890927e8ea8995414bac"  # 여기에 OpenWeatherMap API 키를 추가하세요.
        weather_data = get_weather(city, api_key)
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]

        #맵을 생성
        lat = weather_data["coord"]["lat"]
        lon = weather_data["coord"]["lon"]
        weather_map = folium.Map(location=[lat, lon], zoom_start=10)
        folium.Marker([lat, lon], tooltip=f"{city} 날씨 {temp}").add_to(weather_map)

        weather_map.save('static/weather_map.html')

        return render_template("result.html", city=city, temp=temp, feels_like=feels_like)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)