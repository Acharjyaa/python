import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select  # Correctly importing Select

service_obj = Service("C:\\dri\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

select_element = Select(driver.find_element(By.ID, "dropdown-class-example"))
select_element.select_by_visible_text("Option3")
time.sleep(2)
select_element.select_by_index(1)
time.sleep(2)
select_element.select_by_value("option3")
time.sleep(2)
select_element.select_by_visible_text("Option2")
time.sleep(4)

driver.quit()
