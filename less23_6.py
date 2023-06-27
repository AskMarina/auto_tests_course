import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
	return math.log(abs(12 * math.sin(x)))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()

browser.switch_to.window(browser.window_handles[1])
x_element = int(browser.find_element(By.ID, "input_value").text)
result = calc(x_element)
answer_element = browser.find_element(By.ID, "answer")
answer_element.send_keys(result)
button_win2 = browser.find_element(By.TAG_NAME, "button")
button_win2.click()

time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
