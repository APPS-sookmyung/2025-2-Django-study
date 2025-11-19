from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

##아래 네 줄 코드는 약간 기본으로 사용되는 것들임 기본 설정같은..
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'\statc\uploads'

# 업로드 폴더 생성
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('file')
        for file in uploaded_files:
            if file.filename != '':
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        return redirect(url_for('index'))

    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_info = {
            'filename': filename,
            'filesize': os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], filename)),
            'upload_date': datetime.fromtimestamp(os.path.getmtime(os.path.join(app.config['UPLOAD_FOLDER'], filename))).strftime('%Y-%m-%d %H:%M:%S')
        }
        files.append(file_info)

    return render_template('index.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)