from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
try:
    browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, "input_value").text
    res = math.log(abs(12*math.sin(int(x))))
    browser.find_element(By.ID, "answer").send_keys(str(res))
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(5)
    browser.quit()
