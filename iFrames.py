import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

try:
    driver.get("https://the-internet.herokuapp.com/iframe")
    time.sleep(2)

    driver.switch_to.frame("mce_0_ifr")
    msg = driver.find_element(By.ID, "tinymce")
    msg.clear()
    time.sleep(2)
    msg.send_keys("Hello! Am SAJID")
    time.sleep(2)

    driver.switch_to.default_content()
    #driver.switch_to.parent_frame()
    print(driver.find_element(By.XPATH, "//h3").text)

    driver.close()

except Exception as e:
    print(e)
    driver.quit()