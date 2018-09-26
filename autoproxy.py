
import time
import random

from selenium import webdriver

from config import *


proxyList = [
    '110.45.247.229:1080',
    '219.254.34.231:3128',
    '61.97.130.196:51599'

]

options = webdriver.chrome.options.Options()
options.add_argument('--proxy-server='+i)
browser = webdriver.Chrome(chrome_options=options)

# browser.get('http://www.icanhazip.com/')
browser.get(siteURL)

# print(browser.page_source)
print(i)
print('')
time.sleep(30)

browser.quit()
