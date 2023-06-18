import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://demoqa.com/droppable")
driver.implicitly_wait(10)

action = ActionChains(driver)
src = driver.find_element(By.ID, "draggable")
des = driver.find_element(By.ID, "droppable")

action.drag_and_drop(src, des).perform()
time.sleep(2)

driver.win
driver.quit()