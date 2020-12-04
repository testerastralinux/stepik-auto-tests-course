import os
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/file_input.html")

file_name = 'Test.txt'
file_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(file_dir, file_name)

first_name = browser.find_element_by_css_selector("[placeholder='Enter first name']")
first_name.send_keys("First name")

last_name = browser.find_element_by_css_selector("[placeholder='Enter last name']")
last_name.send_keys("Last name")

email = browser.find_element_by_css_selector("[placeholder='Enter email']")
email.send_keys("Email")

file_input = browser.find_element_by_css_selector("[type='file']")
file_input.send_keys(file_path)

submit = browser.find_element_by_class_name("btn")
submit.click()
