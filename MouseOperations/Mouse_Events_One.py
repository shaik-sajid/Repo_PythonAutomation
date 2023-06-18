import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://demoqa.com/buttons")
time.sleep(2)

doubleClickBtn = driver.find_element(By.ID, "doubleClickBtn")
rightClickBtn = driver.find_element(By.ID, "rightClickBtn")

actions = ActionChains(driver)
actions.double_click(doubleClickBtn).perform()
time.sleep(2)

actions.context_click(rightClickBtn).perform()
time.sleep(2)

driver.quit()