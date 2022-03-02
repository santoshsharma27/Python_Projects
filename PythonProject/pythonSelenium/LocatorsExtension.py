from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

#driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("Rahul")
driver.find_element_by_css_selector(".password").send_keys("shetty")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
#//tagname[text()=’xxx’]
driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
