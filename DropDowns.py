import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

try:
    driver.get("https://www.facebook.com/")
    time.sleep(1)

    driver.find_element(By.LINK_TEXT, "Create new account").click()
    time.sleep(3)

    day = Select(driver.find_element(By.ID, "day"))
    day.select_by_value("25")
    time.sleep(1)

    month = Select(driver.find_element(By.ID, "month"))
    month.select_by_value("1")
    time.sleep(1)

    year = Select(driver.find_element(By.ID, "year"))
    year.select_by_value("1996")
    time.sleep(1)

except Exception as e:
    print(e)
    driver.quit()