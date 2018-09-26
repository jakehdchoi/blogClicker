# https://codelike.pro/create-a-crawler-with-rotating-ip-proxy-in-python/

import random
# import urllib
import random

from urllib.request import Request, urlopen, build_opener
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from config import *


ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port]

# Main function
def main():
    # Retrieve latest proxies
    proxies_req = Request('https://www.sslproxies.org/')
    proxies_req.add_header('User-Agent', ua.random)
    proxies_doc = urlopen(proxies_req).read().decode('utf8')

    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

    # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
          'ip':   row.find_all('td')[0].string,
          'port': row.find_all('td')[1].string
        })

    # Choose a random proxy
    proxy_index = random_proxy()
    proxy = proxies[proxy_index]

    for n in range(100):
        req = Request('http://icanhazip.com')
        req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')

        # Every request, generate a new proxy
        # if n % 1 == 0:
        proxy_index = random_proxy()
        proxy = proxies[proxy_index]

        # Make the call
        try:
            my_ip = urlopen(req).read().decode('utf8')
            print('#' + str(n) + ': ' + my_ip)
        except: # If error, delete this proxy and find another one
            del proxies[proxy_index]
            print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' deleted.')
            proxy_index = random_proxy()
            proxy = proxies[proxy_index]


        opener = build_opener()
        opener.addheaders = [('User-agent', ua.random)]
        print(opener)

        opener.open(siteURL)
        sleep_time = random.randint(31, 60)
        print('sleep_time: ' + str(sleep_time) + 's')
        time.sleep(sleep_time)


# Retrieve a random index proxy (we need the index to delete it if not working)
def random_proxy():
    return random.randint(0, len(proxies) - 1)

if __name__ == '__main__':
    main()
