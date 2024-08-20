import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\\dri\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys('cu')
time.sleep(2)
driver.find_element(By.XPATH,"(//button[@type='button'])[2]").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,"input[type='search']").clear()
time.sleep(4)
