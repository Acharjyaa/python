import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#service_obj="C:\dri\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service_obj = "C:\\dri\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
driver= webdriver.Chrome(service=Service(service_obj))
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(4)







