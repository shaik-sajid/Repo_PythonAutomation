import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

try:
    driver.get("https://demoqa.com/browser-windows")
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "windowButton").click()
    time.sleep(2)

    driver.find_element(By.ID, "messageWindowButton").click()
    time.sleep(2)
    windowHandles = driver.window_handles
    print(windowHandles)

    driver.switch_to.window(windowHandles[1])
    time.sleep(2)
    print("Switched to 1st window")

    driver.switch_to.window(windowHandles[2])
    print("Switched to 2st window")
    time.sleep(2)

    for i in range(len(windowHandles)):
        driver.switch_to.window(windowHandles[i])
        driver.close()
        time.sleep(2)
except Exception as e:
    print(e)
    driver.quit()