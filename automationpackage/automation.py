import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="/Users/codemen/Documents/browserdriver/chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.NAME,"Submit").click()

# code for users add
driver.find_element(By.ID,"menu_admin_viewAdminModule").click()
driver.find_element(By.ID,"menu_admin_viewSystemUsers").click()
