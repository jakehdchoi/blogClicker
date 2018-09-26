
import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from config import *


# def blogVisiter():
#     url = siteURL
#     print("DRIVER IS Firefox")
#     driver = webdriver.Firefox()
#     print("GETTING kproxy")
#     # driver.get("https://whoer.net/webproxy")
#     driver.get("https://hide.me/en/proxy")
#
#     ###############    FIND ELEMENT ID MAINTEXTFIELD ####
#     #elem = driver.find_element_by_id("maintextfield")
#
#     ###############  FIND AND CLEAR FIELD OF ELEMENT NAME MAINTEXTFIELD  ####
#     #print("FINDING AND CLEARING ELEMENT")
#     # elem = driver.find_element_by_id('u').clear()
#
#     ###############     SEND URL VAR TO MAINTEXTFIELD ###
#     elem = driver.find_element_by_id("u").send_keys(url)
#     #send_url = elem.send_keys(url)
#     #send_url
#     ###############  RETURN KEY PRESS
#     elem = driver.find_element_by_id("u").send_keys(Keys.ENTER)
#     ###############  FIND ELEMENT BY CLASS NAME BOTON
#     #elem = driver.find_element_by_class_name("boton")
#     ###############  CLICK ON ELEMENT
#     #elem.click()
#     time.sleep(30)
#     driver.quit()



# def main():
#     blogVisiter()



def main():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", "46.105.57.149")
    profile.set_preference("network.proxy.socks_port", 37035)

    profile.update_preferences()

    driver = webdriver.Firefox(profile)
    # driver = webdriver.Firefox()

    # driver.get('http://www.icanhazip.com/')
    driver.get(siteURL)

    # print(driver.page_source)


    time.sleep(2)
    driver.quit()

    # print(random.randint(2000,9999))


if __name__ == "__main__":
    main()
