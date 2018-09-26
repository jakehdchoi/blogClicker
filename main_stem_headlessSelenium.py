# https://gist.github.com/DusanMadar/8d11026b7ce0bce6a67f7dd87b999f6b

import requests
import time
import os
import random

from stem import Signal
from stem.control import Controller
from selenium import webdriver

from config import *




os.system("sudo service tor restart")
os.system("sudo service privoxy restart")


options = webdriver.chrome.options.Options()
options.add_argument('--proxy-server=127.0.0.1:8118')
options.add_argument('--headless')

response = requests.get('https://api.ipify.org', proxies={'https': '127.0.0.1:8118'})
after = response.text.strip()


for i in range(100):
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

        sleep_time = random.randint(20, 70)
        print('sleep_time: ' + str(sleep_time) + 's')

        browser.get(siteURL)

        time.sleep(sleep_time)
        browser.quit()
