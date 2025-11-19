from flask import Flask, render_template, request
# pip install python-docs
from docx import Document

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def certificate():
    if request.method == "POST":
        name = request.form.get('name')
        course = request.form.get('course')
        email = request.form.get('email')

        doc = Document("templates.docx")

        for paragraph in doc.paragraphs:
            if 'NAME' in paragraph.text:
                paragraph.text = paragraph.text.replace('NAME', name)
            if 'COURSE' in paragraph.text:
                paragraph.text = paragraph.text.replace('COURSE', course)
            if 'EMAIL' in paragraph.text:
                paragraph.text = paragraph.text.replace('EMAIL', email)
        doc.save(f"{name}_{course}_certificate.docx")
        return "보고서가 잘 생성 되었습니다."        

    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)