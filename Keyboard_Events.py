import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

try:
    driver.get("https://www.gmail.com/")
    time.sleep(1)

    createNewAccount = driver.find_element(By.XPATH, "//*[contains(text(),'Create account')]")
    createNewAccount.click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//*[contains(text(),'For my personal use')]").click()
    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    pwd = driver.find_element(By.NAME, "Passwd")
    cpwd = driver.find_element(By.NAME, "ConfirmPasswd")

    username.send_keys("shaiksajid9336")
    act = ActionChains(driver)

    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    time.sleep(1)
    act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
    time.sleep(1)

    pwd.click()
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(1)

    cpwd.click()
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
    time.sleep(2)
except:
    driver.quit()