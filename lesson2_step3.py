from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)

    result = num1 + num2

    dropdown = Select(browser.find_element_by_id("dropdown"))
    dropdown.select_by_value(str(result))

    submit = browser.find_element_by_css_selector("button")
    submit.click()

finally:
    time.sleep(15)
    browser.quit()
