from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    url = f'http://www.omdbapi.com/?s={query}&apikey=b696f5ed'
    response = requests.get(url)
    data = response.json()

    movies = []
    for movie in data['Search']:
        title = movie['Title']
        year = movie['Year']
        poster = movie['Poster']
        movies.append({'title': title, 'year': year, 'poster': poster})

    return render_template('result.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
