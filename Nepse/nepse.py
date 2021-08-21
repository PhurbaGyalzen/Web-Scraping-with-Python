import requests
from bs4 import BeautifulSoup


headers = {
    'Host': 'www.nepalstock.com',
    'Origin': 'http://www.nepalstock.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}


def get_stock(company_id):
    r = requests.get(
        f'http://www.nepalstock.com/company/display/{company_id}', headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    date = soup.find(id='date').text.split(" ")

    table_rows = soup.find('table', class_='my-table').find_all('tr')

    table_data = [data.find_all('td') for data in table_rows]

    info = {
        'company_name': table_data[0][0].text,
        'last_traded_price': table_data[7][1].text,
        'change': table_data[8][1].text,
        'market_closing_price': table_data[12][1].text,
        'date': date[2] + " " + date[5]
    }

    print(info)


my_company = [4956, 2919]

for id in my_company:
    get_stock(id)
