import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element_by_tag_name("button")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value").text
    result = calc(x)

    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(result)

    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
