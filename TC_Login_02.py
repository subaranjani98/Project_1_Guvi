from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver = webdriver.Chrome()
driver.get(url)

driver.maximize_window()

sleep(5)

webelement_of_email_input= driver.find_element(By.XPATH, '//input[@name="username"]')
webelement_of_email_input.send_keys("Admin")

webelement_of_password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
webelement_of_password_input.send_keys("admin124")

sleep(5)

webelement_of_login_button = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')
webelement_of_login_button.click()

sleep(5)

except_msg = 'Invalid credentials'

error_msg_box = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p')
displayed_error = error_msg_box.text

assert displayed_error == except_msg, "displayed error is not as expected"
print("A vaild error message for invalid credentials is displayed.")