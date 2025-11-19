from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lon=10.99&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        city = request.form['city']
        api_key = "bae1df25c37b890927e8ea8995414bac"
        weather_data = get_weather(city, api_key)
        if weather_data["cod"] == 200: 
            temperature = weather_data['main']['temp']
            feels_temp = weather_data['main']['feels_like']
            return render_template('result.html', city=city, temperature=temperature, feels_temp=feels_temp)
        else:
            error_message = "날씨 정보를 가져오는 중에 오류가 발생하였습니다."
            return render_template("error.html", error_message=error_message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
