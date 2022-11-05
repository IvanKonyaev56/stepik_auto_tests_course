from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestStepic(unittest.TestCase):
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your name']")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input2.send_keys("ivan@ivan")

        input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone']")
        input3.send_keys("+79619007536")

        input4 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address']")
        input4.send_keys("Orenburg")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
        button.click()

        # Проверяем, что смогли зарегистрироваться ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be right text")


if __name__ == "__main__":
    unittest.main()
