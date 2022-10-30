from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Вставить значение Имя в форму
    input1 = browser.find_element(By.CSS_SELECTOR, "[name=firstname]")
    input1.send_keys('Ivan')

    # Вставить значение Фамилия в форму
    input2 = browser.find_element(By.CSS_SELECTOR, "[name=lastname]")
    input2.send_keys('Ivanov')

    # Вставить значение Email в форму
    input3 = browser.find_element(By.CSS_SELECTOR, "[name=email]")
    input3.send_keys('1@1')

    # Загрузить файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "Origin.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    # Нажать на кнопку Submit
    option3 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()