import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By





def calc(x):
	return str(math.log(abs(12 * math.sin(x))))


link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text;
print(x)
y = calc(int(x))
y_element = browser.find_element(By.ID, "answer")
y_element.send_keys(y)

option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
option1.click()

option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

# y = calc(x)
