import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service_obj = Service("C:\\dri\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#driver.execute_script("window.scrollBy(0,500)")
#time.sleep(3)
#driver.execute_script("window.scrollBy(0,0)")
#time.sleep(3)
#element=driver.find_element(By.ID,"confirmbtn")
#driver.execute_script("arguments[0].scrollIntoView();", element)
#driver.close()
driver.execute_script("window.open('','_blank')")
time.sleep(2)
driver.execute_script("window.open('https://www.facebook.com/')")
time.sleep(4)