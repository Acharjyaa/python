import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service_obj = Service("C:\\dri\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.current_window_handle)
driver.switch_to.frame("courses-iframe")
time.sleep(5)
value=driver.find_element(By.LINK_TEXT,"Courses")
time.sleep(5)
print(value.text)
time.sleep(5)
driver.switch_to.parent_frame()
time.sleep(5)

