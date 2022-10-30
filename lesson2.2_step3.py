from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму.
    number1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    number2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    number1_text = number1.text
    number2_text = number2.text
    answer = int(number1_text) + int(number2_text)

    # Выбрать в выпадающем списке соответствующее значение.
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(answer))

    # Нажать на кнопку Submit
    option3 = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()