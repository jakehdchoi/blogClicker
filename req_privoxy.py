
import requests
import time
import os
import random

from stem import Signal
from stem.control import Controller

from config import *


os.system("sudo service tor restart")
os.system("sudo service privoxy restart")


response = requests.get('https://api.ipify.org', proxies={'https': '127.0.0.1:8118'})
after = response.text.strip()

for i in range(100):

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

    sleep_time = random.randint(20, 60)
    print('sleep_time: ' + str(sleep_time) + 's')

    res = requests.get(siteURL)
    print('')
    time.sleep(sleep_time)
