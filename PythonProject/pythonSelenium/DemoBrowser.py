from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

#driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")
driver.get("https://www.facebook.com")
driver.back()
driver.refresh()
print(driver.title)
print(driver.current_url)
driver.close()
