from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_options = webdriver.ChromeOptions
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

s = Service("C:\\chromedriver_win32\\chromedriver.exe", options=chrome_options)
driver = webdriver.Chrome(service=s)
#driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)