from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize the browser driver
driver = webdriver.Chrome()
# Navigate to the target webpage
driver.get("https://the-internet.herokuapp.com/login")
driver.implicitly_wait(2.0)
# Identify the form elements and simulate user input
# username = driver.find_element_by_id("username")
username = driver.find_element(by=By.ID, value="username")
username.send_keys("tomsmith")
password = driver.find_element(by=By.ID, value="password")
password.send_keys("SuperSecretPassword!")
# Login to the form
login_button = driver.find_element(by=By.ID, value="login")
login_button.click()
# Close the browser
driver.close()