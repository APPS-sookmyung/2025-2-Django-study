import requests

API_KEY = 'b696f5ed'
URL = 'http://www.omdbapi.com/'

# 영화 검색어 입력 받기
search = input('Enter a movie title: ')

# 영화 정보 검색
params = {'apikey': API_KEY, 's': search}
response = requests.get(URL, params=params)
data = response.json()

# 검색 결과에서 무작위로 영화 선택
if 'Search' in data:
    movies = data['Search']
    movie = movies[0]  # 첫 번째 검색 결과 선택
else:
    print('No movie found.')
    exit()

# 선택한 영화 정보 출력
params = {'apikey': API_KEY, 'i': movie['imdbID']}
response = requests.get(URL, params=params)
data = response.json()

print('Title:', data['Title'])
print('Director:', data['Director'])
print('Actors:', data['Actors'])
print('Plot:', data['Plot'])