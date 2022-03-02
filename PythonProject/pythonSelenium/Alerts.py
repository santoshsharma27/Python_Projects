from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
#driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
validateText = "Option3"
driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alert = driver._switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept()
