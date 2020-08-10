from selenium import webdriver
from config import USERNAME, PASSWORD
import time

browser = webdriver.Chrome(executable_path='/home/safwan/chromedriver_linux64/chromedriver')

browser.maximize_window()
browser.get('http://www.instgram.com')

time.sleep(2)

username = browser.find_element_by_name('username')
username.send_keys(USERNAME)

password = browser.find_element_by_name('password')
password.send_keys(PASSWORD)