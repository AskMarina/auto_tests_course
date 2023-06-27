import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
	return math.log(abs(12 * math.sin(x)))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
text = WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button = browser.find_element(By.ID, "book")
button.click()
inp_x = int(browser.find_element(By.ID, "input_value").text)
result = calc(inp_x)
answer_el = browser.find_element(By.ID, "answer")
answer_el.send_keys(result)
button_solve = browser.find_element(By.ID, "solve")
button_solve.click()

# time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

