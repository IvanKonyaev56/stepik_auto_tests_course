from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    wait = WebDriverWait(browser, 12)
    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажать на кнопку Book
    option1 = browser.find_element(By.CSS_SELECTOR, "#book")
    option1.click()

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
    option2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    option2.click()

finally:
    print(browser.switch_to.alert.text)
    # # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
