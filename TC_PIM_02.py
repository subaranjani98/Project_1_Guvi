from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver = webdriver.Chrome()

driver.get(url)

driver.maximize_window()

sleep(3)

webelement_of_email = driver.find_element(By.XPATH, '//input[@name="username"]')
webelement_of_email.send_keys("Admin")



webelement_of_password = driver.find_element(By.XPATH, '//input[@type="password"]')
webelement_of_password.send_keys("admin123")
sleep(5)

webelement_of_login_button = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')
webelement_of_login_button.click()
sleep(5)

print("The user is logged in successfully.")

pim_lable = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
pim_lable.click()
sleep(5)

print("PIM_clicked")


pim_edit_employee = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]')
pim_edit_employee.click()
sleep(5)

print("pim_edit_employee")


employee_other_id = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')
employee_other_id.send_keys("659")
sleep(5)

print('emplyee_other_id')


employee_driver_number = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')
employee_driver_number.send_keys("0231")
sleep(4)

print('emplyee_driver_number')



save_a_employee = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')
save_a_employee.click()
sleep(3)

print('The user should be able to edit an existing employee information in the PIM and should see a message for successful employee details addition.')
