import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

firstname = browser.find_element(By.NAME, "firstname")
firstname.send_keys("firstname")

lastname = browser.find_element(By.NAME, "lastname")
lastname.send_keys("lastname")

email = browser.find_element(By.NAME, "email")
email.send_keys("email")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'Test1.txt')
# отправляем файл
element = browser.find_element(By.ID, "file")
element.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "button")
button.click()
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

