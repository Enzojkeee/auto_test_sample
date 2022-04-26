from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")
try:
    browser.find_element_by_tag_name("button").click()
    browser.switch_to.alert.accept()
    x = browser.find_element_by_css_selector("#input_value")
    res = math.log(abs(12*math.sin(int(x.text))))
    browser.find_element_by_css_selector("#answer").send_keys(str(res))
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(5)
    browser.quit()

