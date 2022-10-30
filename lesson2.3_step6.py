from selenium import webdriver
from selenium.webdriver.common.by import By
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку I want to go on a magical journey!
    option0 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    option0.click()

    # Перейти на другую вкладку.
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # # Нажать на кнопку I want to go on a magical journey!
    # option1 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    # option1.click()
    #
    # # Принять confirm
    # confirm = browser.switch_to.alert
    # confirm.accept()

    # Посчитать сумму.
    number1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    number1_text = number1.text

    # Решить уравнение.
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(number1_text)

    # Вставить значение y в форму
    input1 = browser.find_element(By.CSS_SELECTOR, "[id=answer]")
    input1.send_keys(y)

    # Нажать на кнопку Submit
    option3 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    option3.click()

finally:
    print(browser.switch_to.alert.text)
    # # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()