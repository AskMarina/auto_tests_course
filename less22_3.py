import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x1, x2):
	return int(x1) + x2


link = "https://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, "num1")
x1 = int(num1.text)
print(x1)
num2 = browser.find_element(By.ID, "num2")
x2 = int(num2.text)
print(x2)

sum_num = calc(x1, x2)

print("sum = ", sum_num)
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(sum_num)) # ищем элемент с текстом с посчитанной суммой

button = browser.find_element(By.CSS_SELECTOR, "button")
button.click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()


