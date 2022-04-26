from selenium import webdriver
import time
import os
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
try:
    browser.find_element_by_name("firstname").send_keys("Vladimir")
    browser.find_element_by_name("lastname").send_keys("Kaz")
    browser.find_element_by_name("email").send_keys("test@mail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element_by_name("file").send_keys(file_path)
    browser.find_element_by_css_selector(".btn").click()
finally:
    time.sleep(3)
    browser.quit()
