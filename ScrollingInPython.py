import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://www.amazon.in")
time.sleep(2)

driver.execute_script("window.scrollBy(0, 500)")
time.sleep(2)
driver.execute_script("window.scrollBy(0, -500)")
time.sleep(2)

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(2)

driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")
time.sleep(2)

driver.quit()