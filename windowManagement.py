import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)


driver.get("https://www.linkedin.com/")
time.sleep(2)

print("Window size ", driver.get_window_size())
driver.set_window_size(700, 700)
time.sleep(2)

print("Window position", driver.get_window_position())
driver.set_window_position(500, 100)
time.sleep(2)
driver.quit()