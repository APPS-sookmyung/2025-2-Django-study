from flask import Flask, render_template, request
import requests

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
        api_key = "3a6f80e289e1493a5d11e6216a1cafbf"
        if weather_data["cod"] == 200:
            temperature = weather_data["main"]["temp"]
            return render_template("result.html", city=city, temperature=temperature)
        else:
            error_message = "날씨 정보를 가져오는 중에 오류가 발생했습니다."
            return render_template("error.html", error_message=error_message)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()