from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver = webdriver.Chrome()

driver.get(url)

driver.maximize_window()

sleep(2)

webelement_of_email_input = driver.find_element(By.XPATH, '//input[@name="username"]')
webelement_of_email_input.send_keys("Admin")



webelement_of_password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
webelement_of_password_input.send_keys("admin123")

sleep(3)

webelement_of_login_button = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')
webelement_of_login_button.click()

sleep(3)
print("The user is logged in successfully.")

pim_lable = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
pim_lable.click()
print("PIM_clicked")
sleep(3)

pim_check_box_employee = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/label/span/i')
pim_check_box_employee.click()
# print("pim_check_box_employee")
sleep(3)

employee_delete_selected = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/button/i')
employee_delete_selected.click()
print('employee_delete_selected')
sleep(2)


delete_the_employee = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
delete_the_employee.click()
print('The user should be able to delete an existing employee information in the PIM and should see a message for successful deletion.')
sleep(5)