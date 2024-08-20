import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\\dri\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radiobutton1=driver.find_element(By.CSS_SELECTOR,"input[value='radio1']")
print("before selection of radio button 1",radiobutton1.is_selected())  # False
time.sleep(2)
radiobutton1.click()
time.sleep(2)
print("after selection of radio button 1",radiobutton1.is_selected()) #True
time.sleep(3)
radiobutton3=driver.find_element(By.CSS_SELECTOR,"input[value='radio3']")
print("before selecting the radio button 3 value is",radiobutton3.is_selected()) # False
radiobutton3.click()
time.sleep(2)
print("after selecting radio button 3 ",radiobutton3.is_selected()) # True
print("after selecting radio button 3 value of radion button 1",radiobutton1.is_selected()) # False





import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# var1=driver.find_element(By.CSS_SELECTOR,"#checkBoxOption3").is_selected()
# print(var1)   # False
# driver.find_element(By.CSS_SELECTOR,"#checkBoxOption3").click()
# time.sleep(3)
# var2=driver.find_element(By.CSS_SELECTOR,"#checkBoxOption3").is_selected()
# print(var2) #True
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1").click()
# time.sleep(3)
# var3= driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1").is_selected()
# print("this is last selected element of option 1",var3) #True
# print("This is first selected element of option 3",driver.find_element(By.CSS_SELECTOR,"#checkBoxOption3").is_selected()) # True

# for the radio buttons
radiobutton1=driver.find_element(By.CSS_SELECTOR,"input[value='radio1']")
print("before selection of radio button 1",radiobutton1.is_selected())  # False
time.sleep(2)
radiobutton1.click()
time.sleep(2)
print("after selection of radio button 1",radiobutton1.is_selected()) #True
time.sleep(3)
radiobutton3=driver.find_element(By.CSS_SELECTOR,"input[value='radio3']")
print("before selecting the radio button 3 value is",radiobutton3.is_selected()) # False
radiobutton3.click()
time.sleep(2)
print("after selecting radio button 3 ",radiobutton3.is_selected()) # True
print("after selecting radio button 3 value of radion button 1",radiobutton1.is_selected()) # False







from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Select(driver.find_element(By.TAG_NAME,"Select")).select_by_visible_text("Option3")
# Select(option).select_by_index(1)
# Select(option).select_by_value("option3")
# Select(option).select_by_visible_text("Option2")
time.sleep(4)











import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.current_window_handle)
driver.find_element(By.LINK_TEXT,"Open Tab").click()
time.sleep(3)
driver.find_element(By.ID,"openwindow").click()
all_windows= driver.window_handles
driver.switch_to.window(all_windows[1])
driver.find_element(By.LINK_TEXT,"Access all our Courses").click()
time.sleep(4)
driver.switch_to.window(all_windows[0])
driver.find_element(By.ID,"checkBoxOption2").click()
time.sleep(4)

driver.switch_to.window(all_windows[2])
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Access all our Courses").click()
time.sleep(3)




import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
driver.switch_to.frame("courses-iframe")
value= driver.find_element(By.LINK_TEXT,"Courses")
print(value.text)
driver.switch_to.parent_frame()
time.sleep(2)
driver.find_element(By.ID,"checkBoxOption2").click()
time.sleep(3)

# for changing multiple frames and switch to parent
#driver.switch_to.default_content



import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action= ActionChains(driver)
element=driver.find_element(By.ID,"mousehover")
action.move_to_element(element).perform()
driver.find_element(By.LINK_TEXT,"Reload").click()
time.sleep(3)


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
# # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# # driver.execute_script("window.scrollBy(0,600)")
# element= driver.find_element(By.ID,"confirmbtn")
# driver.execute_script("arguments[0].scrollIntoView();",element)
# # time.sleep(2)
# # driver.execute_script("window.scrollTo(0,0)")
# time.sleep(3)
# driver.close()

# for opening new window
# driver.execute_script("window.open('','_blank')")
# time.sleep(1)
# driver.execute_script("window.open('https://www.facebook.com/')")
# time.sleep(3)
# driver.close()




[7:51 pm, 27/7/2024] Tushar Patil: import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
time.sleep(3)
source= driver.find_element(By.XPATH,"//div[@id='draggable']")
destination=driver.find_element(By.XPATH,"//div[@id='droppable']")
action= ActionChains(driver)
# action.drag_and_drop(source,destination).perform()
action.drag_and_drop_by_offset(source,120,90).perform()
time.sleep(4)
[7:51 pm, 27/7/2024] Tushar Patil: implicite wait and explicite wait



import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait= WebDriverWait(driver,10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
driver.find_element(By.XPATH,"//div[@class='products']/div[3]/div/button[text()='ADD TO CART']").click()
driver.find_element(By.XPATH,"//div[@class='products']/div[1]/div/button[text()='ADD TO CART']").click()
driver.find_element(By.CSS_SELECTOR,".search-keyword").clear()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("cuc")
driver.find_element(By.XPATH,"//div[@class='products']/div/div/button[text()='ADD TO CART']").click()
driver.find_element(By.XPATH,'//img[@class=" "]').click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("apply50")
# driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".promoBtn"))).click()
value=driver.find_element(By.CSS_SELECTOR,".promoInfo")
print(value.text)



import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/FileUpload.html")
time.sleep(4)
file_upload= driver.find_element(By.ID,"input-4")
file_upload.send_keys("C:\\Users\\admin\Desktop\\file_upload\practice.webp")
time.sleep(4)

