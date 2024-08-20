import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service_obj = "C:\\dri\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
driver = webdriver.Chrome(service=Service(service_obj))
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH, value="//input[@name='email']").send_keys("sushree.acharjya97@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH, value="//input[@type='password']").send_keys("Bishnupriy2")
time.sleep(3)
driver.find_element(By.XPATH,value="//button[@name='login']").click()
time.sleep(4)
driver.back()
time.sleep(3)

