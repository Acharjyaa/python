import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
service_obj = Service("C:\\dri\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://flipkart.com/")
driver.maximize_window()
time.sleep(2)
action = ActionChains(driver)
element = driver.find_element(By.XPATH, '//img[@alt="Fashion"]')
action.move_to_element(element).perform()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Men Footwear").click()
time.sleep(2)
driver.close()

