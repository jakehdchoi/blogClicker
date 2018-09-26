# http://www.thedurkweb.com/automated-anonymous-interactions-with-websites-using-python-and-tor/

import stem.process

from stem import Signal
from stem.control import Controller
from splinter import Browser

from config import *

proxyIP = "127.0.0.1"
proxyPort = 9150

proxy_settings = {"network.proxy.type":1,
    "network.proxy.ssl": proxyIP,
    "network.proxy.ssl_port": proxyPort,
    "network.proxy.socks": proxyIP,
    "network.proxy.socks_port": proxyPort,
    "network.proxy.socks_remote_dns": True,
    "network.proxy.ftp": proxyIP,
    "network.proxy.ftp_port": proxyPort
}
browser = Browser('firefox', profile_preferences=proxy_settings)
browser.visit("http://www.icanhazip.com")

def switchIP():
    with Controller.from_port(port=9151) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def interactWithSite(browser, deduplication):
    browser.visit(siteURL)
    # browser.fill("comment", "But the thing is... Why would anyone ever want to do this? I must have thought that "+str(deduplication)+" times...")
    # browser.fill("author", "Pebblor El Munchy")
    # browser.fill("email", "barack@tehwhitehouz.gov")
    # browser.fill("url", "https://upload.wikimedia.org/wikipedia/en/1/16/Drevil_million_dollars.jpg")
    # button = browser.find_by_name("submit")
    # button.click()

for x in range(10):
    print(str(x)+': start\n')
    interactWithSite(browser, x)
    switchIP()
    time.sleep(5)
