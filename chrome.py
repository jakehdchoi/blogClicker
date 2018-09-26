import time
from selenium import webdriver
from config import *

driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
# or '/usr/lib/chromium-browser/chromedriver' if you use chromium-chromedriver
driver.get(siteURL);
time.sleep(5) # Let the user actually see something!
driver.quit()
