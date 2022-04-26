from selenium import webdriver
import time
import math

try:  
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    xtext = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = xtext.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x = calc(x)
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(x)
    cbox = browser.find_element_by_css_selector("#robotCheckbox")
    cbox.click()
    rbut = browser.find_element_by_css_selector("#robotsRule")
    rbut.click()
    button = browser.find_element_by_css_selector(".btn")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
