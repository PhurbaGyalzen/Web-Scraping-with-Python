import requests
from bs4 import BeautifulSoup
import pandas as pd

book_details = []
s = requests.Session()

for page in range(1,51):
    print("scraping page number", page)
    url = f'https://books.toscrape.com/catalogue/page-{page}.html'
    headers = {
        'User-Agent': 	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    }

    r = s.get(url,headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.find_all('a')[1]['title']
        price = book.find('p', class_='price_color').text[2:]
        stock = book.find('p', class_='instock availability').text.strip()
        
        detail = {
            'title': title,
            'price': price,
            'stock': stock,
        }
        book_details.append(detail)

df = pd.DataFrame(book_details)
df.to_csv('books.csv', index = False)
print("Scraping complete!!!")