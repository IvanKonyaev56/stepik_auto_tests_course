from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти элемент-картинку.
    find_picture = browser.find_element(By.CSS_SELECTOR, "[id = treasure]")
    find_attribute = find_picture.get_attribute("valuex")

    # Решить уравнение.
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(find_attribute)

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
    option3 = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()