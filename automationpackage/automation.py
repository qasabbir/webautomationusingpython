import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="/Users/codemen/Documents/browserdriver/chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.NAME,"Submit").click()

# code for users add
driver.find_element(By.ID,"menu_admin_viewAdminModule").click()
print(driver.title)
driver.find_element(By.ID,"btnAdd").click()

# this code for selectbox/dropdown
selectbox1 = driver.find_element(By.ID, "systemUser_userType")
selectelement = Select(selectbox1)
selectelement.select_by_visible_text("Admin")

#autocomplete search box handle

driver.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Orange Test")
driver.find_element(By.ID,"systemUser_userName").send_keys("test12101")

# this code for dropdown select by index

selecbox2= driver.find_element(By.ID,"systemUser_status")
selectelementuser = Select(selecbox2)
selectelementuser.select_by_index(0)

driver.find_element(By.ID,"systemUser_password").send_keys("test1234@S!!")
driver.find_element(By.ID,"systemUser_confirmPassword").send_keys("test1234@S!!")

driver.find_element(By.CLASS_NAME, "addbutton").click()
time.sleep(5)
driver.close()