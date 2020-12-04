import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    result = calc(x)

    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(result)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    button = browser.find_element_by_class_name("btn")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
