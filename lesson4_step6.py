from selenium import webdriver
from selenium.common import exceptions

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/cats.html")

try:
    browser.find_element_by_id("button")
except exceptions.NoSuchElementException:
    print("NoSuchElementException")
except exceptions.StaleElementReferenceException:
    print("StaleElementReferenceException")
except exceptions.ElementNotVisibleException:
    print("ElementNotVisibleException")
finally:
    browser.quit()
