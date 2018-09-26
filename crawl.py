
import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from config import *

i = 0

def blogVisiter():
    for i in range(20):
        url = siteURL
        print("DRIVER IS Chrome")
        driver = webdriver.Firefox()
        # driver = webdriver.Chrome()
        print("GETTING kproxy server"+str(i+1))
        driver.get('https://kproxy.com/')

        ###############    FIND ELEMENT ID MAINTEXTFIELD ####
        #elem = driver.find_element_by_id("maintextfield")

        ###############  FIND AND CLEAR FIELD OF ELEMENT NAME MAINTEXTFIELD  ####
           #print("FINDING AND CLEARING ELEMENT")
        elem = driver.find_element_by_id('maintextfield').clear()

        ###############     SEND URL VAR TO MAINTEXTFIELD ###
        elem = driver.find_element_by_id("maintextfield").send_keys(url)
        #send_url = elem.send_keys(url)
        #send_url
        ###############  RETURN KEY PRESS
        elem = driver.find_element_by_id("maintextfield").send_keys(Keys.ENTER)
        ###############  FIND ELEMENT BY CLASS NAME BOTON
        #elem = driver.find_element_by_class_name("boton")
        ###############  CLICK ON ELEMENT
        #elem.click()
        time.sleep(20)
        driver.quit()



def main():
    blogVisiter()



# def main():
#     for i in range(5):
#         # profile = webdriver.FirefoxProfile()
#         # profile.set_preference("network.proxy.type", 1)
#         # profile.set_preference("network.proxy.socks", "Host")
#         # profile.set_preference("network.proxy.socks_port", random.randint(2000,9999))
#         #
#         # profile.update_preferences()
#         #
#         # driver = webdriver.Firefox(profile)
#         driver = webdriver.Firefox()
#
#         driver.get('http://www.icanhazip.com/')
#         # driver.get(siteURL)
#
#         print(driver.page_source)
#
#         driver.quit()
#
#         time.sleep(2)
#
#     # print(random.randint(2000,9999))


if __name__ == "__main__":
    main()
