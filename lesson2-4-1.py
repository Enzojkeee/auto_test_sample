from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


try:
    price = WebDriverWait(browser, 11).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()
    x= browser.find_element(By.ID, "input_value").text
    res = math.log(abs(12*math.sin(int(x))))
    browser.find_element(By.ID, "answer").send_keys(str(res))
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(3)
    browser.quit()
