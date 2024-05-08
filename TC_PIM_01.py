from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver = webdriver.Chrome()

driver.get(url)

driver.maximize_window()

sleep(3)

webelement_of_email_input = driver.find_element(By.XPATH, '//input[@name="username"]')
webelement_of_email_input.send_keys("Admin")


webelement_of_password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
webelement_of_password_input.send_keys("admin123")
sleep(5)

webelement_of_login_button = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')
webelement_of_login_button.click()
sleep(3)

print("The user is logged in successfully.")

pim_lable = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
pim_lable.click()
sleep(5)

print("PIM_clicked")


pim_add_employee = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
pim_add_employee.click()
sleep(5)

print("pim_add_employee")


employee_new_person_first_name = driver.find_element(By.XPATH, '//input[@name="firstName"]')
employee_new_person_first_name.send_keys("Bharathi")
sleep(2)

print('employee_new_person_first_name')


employee_new_person_middle_name = driver.find_element(By.XPATH, '//input[@name="middleName"]')
employee_new_person_middle_name.send_keys("Raja")
sleep(5)

print('employee_new_person_middle_name')


employee_new_person_last_name = driver.find_element(By.XPATH, '//input[@name="lastName"]')
employee_new_person_last_name.send_keys("P")
sleep(5)

print('employee_new_person_last_name')


save_a_employee = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
save_a_employee.click()
sleep(5)

print("The user should be able to add a new employee in the PIM and should see a message for successful employee addition.")
