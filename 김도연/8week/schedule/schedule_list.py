from flask import Flask, request, render_template

app = Flask(__name__)

schedule = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        title = request.form['title']
        schedule.append({'start': start, 'end': end, 'title': title})
    return render_template('index.html', schedule=schedule)

if __name__ == '__main__':
    app.run()