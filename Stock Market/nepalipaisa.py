import requests
from bs4 import BeautifulSoup
import json

class MyStock():
    def __init__(self, fromdate, toDate, stockSymbol):
        self.fromdate = fromdate
        self.toDate = toDate
        self.stockSymbol = stockSymbol
        self.records = []

    def getRecords(self):
        url = 'https://www.nepalipaisa.com/Modules/GraphModule/webservices/MarketWatchService.asmx/GetTodaySharePrices'

        s = requests.Session()

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36,'
        }

        payload = {
            'fromdate': self.fromdate, 
            'toDate': self.toDate, 
            'stockSymbol': self.stockSymbol, 
            'offset': 1, 
            'limit': 50
        }

        r = requests.post(url, headers=headers, data= payload)

        soup = BeautifulSoup(r.text, 'lxml')

        details = soup.find_all('todayshareprice')
        for detail in details:
            CompanySymbol = detail.find('stocksymbol').text
            maxprice = detail.find('maxprice').text
            minprice = detail.find('minprice').text
            closingprice = detail.find('closingprice').text
            nooftransaction = detail.find('nooftransaction').text
            totalamount = detail.find('totalamount').text
            difference = detail.find('difference').text
            percentdifference = detail.find('percentdifference').text
            asofdate = detail.find('asofdate').text[:10]
            
            data = {
                'CompanySymbol': CompanySymbol,
                'maxprice': maxprice,
                'minprice': minprice,
                'closingprice': closingprice,
                'nooftransaction': nooftransaction,
                'totalamount': totalamount,
                'difference': difference,
                'percentdifference': percentdifference,
                'asofdate': asofdate
            }

            self.records.append(data)
        s.close()
                
        return self.records

if __name__ == "__main__":
    Stock = MyStock('04/03/2021','05/31/2021','NIFRA')
    records = Stock.getRecords()
    with open('sharerecords.json', 'w') as f:
        json.dump(records, f)