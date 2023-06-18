import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

try:
    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(5)

    email = driver.find_element(By.ID, "email")
    pwd = driver.find_element(By.ID, "pass")

    email.send_keys("9059886469")
    time.sleep(1)
    pwd.send_keys("Karishma@123")
    time.sleep(1)

    driver.find_element(By.NAME, "login").click()
    time.sleep(1)
    driver.set_page_load_timeout(30)

    time.sleep(15)
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@role='banner']/div[3]/div/span")))
    account = driver.find_element(By.XPATH, "//div[@role='banner']/div[3]/div/span")
    account.click()
    time.sleep(1)
    logout = driver.find_element(By.XPATH, "//*[contains(text(),'Log Out')]")
    logout.click()
    time.sleep(1)

except Exception as e:
    print(e)
    driver.close()