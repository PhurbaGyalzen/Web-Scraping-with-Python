import requests
from pprint import pprint
from bs4 import BeautifulSoup


url = "https://www.sslproxies.org"
with requests.Session() as s:
    r = s.get(url)
soup = BeautifulSoup(r.text, "lxml")

proxies = soup.find('tbody').find_all('tr')


def get_proxies():
    pxs = []
    for proxy in proxies:
        str = []
        for p in (proxy.find_all('td')[:2]):
            str.append(p.text)
        value = ":".join(str)
        pxs.append(value)
    return pxs
