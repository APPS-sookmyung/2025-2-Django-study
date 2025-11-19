import googletrans

translator = googletrans.Translator()

input_text = input("번역할 문장을 입력하세요(한글): ")
translated = translator.translate(input_text, dest="en").text
print(f"한글 입력 값: {input_text}")
print(f"영어 번역 값: {translated}")