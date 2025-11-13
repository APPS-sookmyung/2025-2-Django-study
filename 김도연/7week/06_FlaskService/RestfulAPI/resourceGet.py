import requests

def get_data(x, y):
	url = "http://127.0.0.1:8000/minus"
	params = {"x": x, "y":y}
	res = requests.get(url, params=params)
	return res.json()

x = 7
y = 5
print("자료형:", type(get_data(x, y)))
print("API 값:", get_data(x, y))
print("데이터: ", get_data(x, y)["result"])