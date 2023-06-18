import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

try:
    driver.get("https://www.facebook.com")
    time.sleep(3)

    driver.switch_to.new_window('window')
    driver.get("https://www.instagram.com")
    time.sleep(3)

    driver.switch_to.new_window('window')
    driver.get("https://www.linkedin.com")
    time.sleep(3)

    windowHandles = driver.window_handles
    for i in range(len(windowHandles)-1, -1, -1):
        print(i)
        driver.switch_to.window(windowHandles[i])
        print(driver.title)
        driver.close()
        time.sleep(1)

except Exception as e:
    print(e)
    driver.quit()