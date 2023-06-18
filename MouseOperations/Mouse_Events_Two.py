import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://www.myntra.com")
time.sleep(2)
action = ActionChains(driver)
list = driver.find_elements(By.XPATH, "//*[@data-reactid='18']/div")
for li in list:
    action.move_to_element(li).perform()
    time.sleep(1)

driver.quit()