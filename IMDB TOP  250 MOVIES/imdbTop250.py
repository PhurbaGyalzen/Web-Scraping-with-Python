import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = 'https://www.imdb.com/chart/top/'
s = requests.Session()
print('scraping...')
r = s.get(url)

soup = BeautifulSoup(r.text, 'lxml')

movies = soup.find('table', class_='chart full-width').find('tbody').find_all('tr')
position = 0
MovieDetails = []
for movie in movies:
    position += 1
    title = movie.find('td', class_='titleColumn').find('a').text.strip()
    year = movie.find('td', class_='titleColumn').find('span').text.strip()[1:5]
    rating = movie.find('td', class_='ratingColumn imdbRating').text.strip()
    
    detail = {
        'postition': position,
        'title': title,
        'year': year,
        'rating': rating,
    }

    MovieDetails.append(detail)

with open('imdbTop250.json', 'w') as f:
    json.dump(MovieDetails, f)

df = pd.DataFrame(MovieDetails)
df.to_csv('imdbTop250.csv', index = False)

print('Scraping Complete!!!')