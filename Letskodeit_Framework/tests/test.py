import time

from selenium import webdriver

option = webdriver.FirefoxOptions()
option.set_preference("dom.webdriver.enabled", False)
# option.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36')
driver = webdriver.Firefox(options=option)