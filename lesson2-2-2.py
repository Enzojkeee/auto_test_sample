from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
try:
    x= browser.find_element_by_css_selector("#input_value")
    res = math.log(abs(12*math.sin(int(x.text))))
    res = str(res)
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(res)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_css_selector("input[type='checkbox']").click()
    browser.find_element_by_css_selector("#robotsRule").click()
    button.click()
finally:
    time.sleep(5)
    browser.quit()
