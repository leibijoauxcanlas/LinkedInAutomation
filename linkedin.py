import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser=webdriver.Chrome()
browser.get('https://www.linkedin.com/')

ids = browser.find_element_by_id('login-email')
ids.send_keys('email@email.com')#email here

password = browser.find_element_by_id("login-password")
password.send_keys('password')#password here

login = browser.find_element_by_id('login-submit')
login.click()
time.sleep(1)


browser.close()
