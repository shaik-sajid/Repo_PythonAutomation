import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
chromeOptions.add_argument("--ignore-certificate-errors")
service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chromeOptions)
driver.maximize_window()

driver.get("https://shaik-sajid.github.io/CPF/")
time.sleep(2)

driver.get_screenshot_as_file("MyImage.png")

driver.close()