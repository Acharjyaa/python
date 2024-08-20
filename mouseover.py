import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
service_obj = Service("C:\\dri\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)
# Create an instance of ActionChains
action = ActionChains(driver)
# Find the element to hover over
element = driver.find_element(By.ID, "mousehover")
# Hover over the element
action.move_to_element(element).perform()
# Click on the "Reload" link
driver.find_element(By.LINK_TEXT, "Reload").click()
time.sleep(2)
# Close the browser
driver.quit()
