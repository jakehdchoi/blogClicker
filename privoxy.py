# https://gist.github.com/DusanMadar/8d11026b7ce0bce6a67f7dd87b999f6b

import requests
import time
import os
import random

from stem import Signal
from stem.control import Controller
from selenium import webdriver

from urllib.request import build_opener, ProxyHandler
from fake_useragent import UserAgent

from config import *

ua = UserAgent()


selenium_mode = False

# os.system("sudo pidof tor | xargs kill")
# os.system('sudo echo "CookieAuthentication 0" >> /etc/tor/torrc')
os.system("sudo service tor restart")
os.system("sudo service privoxy restart")

options = webdriver.chrome.options.Options()
options.add_argument('--proxy-server=127.0.0.1:8118')

response = requests.get('https://api.ipify.org', proxies={'https': '127.0.0.1:8118'})
after = response.text.strip()

for i in range(100):
    if selenium_mode == True:
        browser = webdriver.Chrome(chrome_options=options)
    print('[' + str(i) + ']')

    before = after
    print(before)

    while before == after:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='my password')
            controller.signal(Signal.NEWNYM)

        response = requests.get('https://api.ipify.org', proxies={'https': '127.0.0.1:8118'})
        after = response.text.strip()
        print(after)

        time.sleep(1)

    if selenium_mode == True:
        sleep_time = random.randint(20, 60)
        print('sleep_time: ' + str(sleep_time) + 's')

        browser.get(siteURL)
        time.sleep(sleep_time)
        browser.quit()
    else:
        opener = build_opener()
        opener.add_handler(ProxyHandler(proxies={'https': '127.0.0.1:8118'}))
        opener.addheaders = [('User-agent', ua.random)]
        # print(opener)

        sleep_time = random.randint(20, 60)
        print('sleep_time: ' + str(sleep_time) + 's')
        opener.open(siteURL)
        time.sleep(sleep_time)
