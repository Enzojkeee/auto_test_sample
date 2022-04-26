from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)
try:
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    res = str(int(num1.text) + int(num2.text))
    print(res)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(res)
    browser.find_element_by_css_selector(".btn").click()
finally:
    time.sleep(5)
    browser.quit()
