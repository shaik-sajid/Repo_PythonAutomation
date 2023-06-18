import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
url = "https://www.linkedin.com"
driver.get(url)
time.sleep(2)
email = driver.find_element(By.ID, "session_key")
password = driver.find_element(By.NAME, "session_password")
email.send_keys("ABC@Gmail.com")
time.sleep(1)
password.send_keys("ABC@123")
time.sleep(1)
loginBtn = driver.find_element(By.XPATH, "((//*[contains(text(),'Sign in')])[2])")
loginBtn.click()
time.sleep(2)
driver.quit()