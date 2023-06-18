import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdrivermanager.chrome import ChromeDriverManager

driver_obj = Service("C://Users/MY/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=driver_obj)
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().download_and_install()))
driver.maximize_window()
driver.get("https://www.facebook.com")
time.sleep(2)
driver.get("https://www.linkedin.com")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
print("current url is ", driver.current_url)
print("title is", driver.title)
time.sleep(2)
driver.close()
