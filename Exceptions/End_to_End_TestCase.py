import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

try:
    url = "https://rahulshettyacademy.com/angularpractice/"
    driver.get(url)
    time.sleep(2)

    shop = driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]")
    shop.click()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 500)")
    time.sleep(2)

    mobiles = driver.find_elements(By.XPATH, "//div[@class='card h-100']/a/img")
    for mobile in mobiles:
        if mobile.get_attribute("src").__contains__("blackberry.jpg"):
            driver.find_element(By.XPATH, "(//button)[5]").click()

    time.sleep(2)
    driver.execute_script("window.scrollBy(0, -500)")
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[contains(text(),'Checkout')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='country']").send_keys("India")
    time.sleep(8)
    driver.find_element(By.XPATH, "//a[contains(text(),'India')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
    time.sleep(2)
    text = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    assert text == '''×
Success! Thank you! Your order will be delivered in next weeks :-).'''
except Exception as e:
    print(e)
    driver.quit()

driver.quit()