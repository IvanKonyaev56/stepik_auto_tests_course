from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму.
    number1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    number1_text = number1.text

    # Решить уравнение.
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(number1_text)

    # Проскроллить страницу вниз.
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Вставить значение y в форму
    input1 = browser.find_element(By.CSS_SELECTOR, "[id=answer]")
    input1.send_keys(y)

    # Поставить галочку в чекбоксе
    option1 = browser.find_element(By.CSS_SELECTOR, "[id=robotCheckbox]")
    option1.click()

    # Выбрать радиокнопку
    option2 = browser.find_element(By.CSS_SELECTOR, "[id=robotsRule]")
    option2.click()

    # Нажать на кнопку Submit
    option3 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()