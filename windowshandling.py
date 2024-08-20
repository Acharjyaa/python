import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service_obj = Service("C:\\dri\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.current_window_handle)
driver.find_element(By.LINK_TEXT, "Open Tab").click()
time.sleep(5)  # Give time for the new tab to open
all_windows = driver.window_handles
driver.switch_to.window(all_windows[1])
driver.find_element(By.LINK_TEXT, "Access all our Courses").click()
time.sleep(3)
driver.switch_to.window(all_windows[0])
time.sleep(5)
driver.find_element(By.ID, "checkBoxOption2").click()
time.sleep(3)
driver.find_element(By.ID, "openwindow").click()
time.sleep(5)  # Give time for the new window to open
all_windows = driver.window_handles
driver.switch_to.window(all_windows[2])
driver.find_element(By.LINK_TEXT, "Access all our Courses").click()
time.sleep(3)
