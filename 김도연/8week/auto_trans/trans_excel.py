from flask import Flask, render_template, request
from flask import send_file
import os
import openpyxl
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('trans_file.html')

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file.save(os.path.join("uploads", file.filename))
    
    # 엑셀 파일을 불러온 뒤 활성화된 시트를 선택
    workbook = openpyxl.load_workbook(os.path.join("uploads", file.filename))
    sheet = workbook.active

    # 구글 번역 기능
    translator = Translator()

    # 각 cell을 선택하여 value 값을 번역
    for row in sheet.iter_rows():
        for cell in row:
            translated_text = translator.translate(cell.value, dest='en').text
            cell.value = translated_text

    # 새로운 엑셀 파일로 저장
    workbook.save('translated_excel.xlsx')
    
    return render_template('result_trans.html', file_name=file.filename)

@app.route('/download_report')
def download_report():
    return send_file('translated_excel.xlsx', as_attachment=True)
    
if __name__ == '__main__':
    app.run(debug=True)