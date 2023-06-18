import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
url = "https://demoqa.com/alerts"
driver.get(url)
time.sleep(3)

simpleAlert = driver.find_element(By.ID, "alertButton")
simpleAlert.click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

confirmAlert = driver.find_element(By.ID, "confirmButton")
confirmAlert.click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)

driver.execute_script("window.scrollBy(0, 500)")
time.sleep(3)

promptAlert = driver.find_element(By.ID, "promtButton")
promptAlert.click()
time.sleep(2)
driver.switch_to.alert.send_keys("Hi Sajid")
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.close()