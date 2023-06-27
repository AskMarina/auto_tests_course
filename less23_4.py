import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
	return math.log(abs(12 * math.sin(x)))


link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button.click()
confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.ID, "input_value").text
result = str(calc(int(x_element)))
answer_element = browser.find_element(By.ID, "answer")
answer_element.send_keys(result)
button_submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
button_submit.click()
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
