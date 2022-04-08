import requests
import concurrent.futures
from collect_proxy_server import get_proxies

proxies = get_proxies()


def extract(proxy):
    try:
        s = requests.get('https://httpbin.org/ip',
                         proxies={'http': proxy, 'https': proxy}, timeout=2)
        print(s.json(), "- working")
        if s.status_code == 200:
            print(proxy)
    except:
        pass
    return proxy


with concurrent.futures.ThreadPoolExecutor() as exector:
    working = exector.map(extract, proxies)
