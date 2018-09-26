# https://www.proxydocker.com/en/socks-list/anonymity/ELITE

import time
import random

from selenium import webdriver
from config import *

proxyList = [
    # ['46.105.57.149',   37035],
    # ['157.119.207.14',  6667],
    # ['121.134.174.236', 4145],
    # ['211.195.241.230', 4145],
    # ['46.105.57.150',   39867],
    # ['192.169.140.100', 58732],
    # ['112.170.31.133',  4145],
    # ['112.184.236.79',  4145],
    # ['70.166.38.71',    24801],
    # ['192.169.202.104', 35766],
    # ['178.151.241.122', 2140,   'Elite'],
    ['46.105.57.150',   36762,  'Elite']

]

number = len(proxyList)

def main():
    for i in range(number):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.socks", proxyList[i][0])
        profile.set_preference("network.proxy.socks_port", proxyList[i][1])

        profile.update_preferences()

        driver = webdriver.Firefox(profile)
        # driver = webdriver.Firefox()

        # driver.get('http://www.icanhazip.com/')
        try:
            driver.get(siteURL)
        except:
            time.sleep(5)
            driver.quit()


        # print(driver.page_source)
        print(proxyList[i])
        print('')

        time.sleep(10)
        driver.quit()

        # print(random.randint(2000,9999))


if __name__ == "__main__":
    main()
