import time

from selenium import webdriver

urllist = [
    ''
]



for i in urllist:
    browser = webdriver.Firefox()
    browser.get(i)
    time.sleep(30)
    browser.close()
