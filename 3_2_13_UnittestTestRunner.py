# Попробуйте оформить тесты из первого модуля в стиле unittest.
#
# Возьмите тесты из шага 1.6_10 и 1.6_11.
# Создайте новый файл
# Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
# Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
# Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
# Запустите получившиеся тесты из файла
# Просмотрите отчёт о запуске и найдите последнюю строчку
# Отправьте эту строчку в качестве ответа на это задание


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        #  Присвоение адреса переменной link
        link = "http://suninjuly.github.io/registration1.html"

        #  Открытие адреса в Chrome
        browser = webdriver.Chrome()
        browser.get(link)

        #  Поиск элемента по значению атрибута class
        input1 = browser.find_element(By.CLASS_NAME, 'form-control.first')
        input1.send_keys("Ivan")

        #  Поиск элемента по значению атрибута class
        input2 = browser.find_element(By.CLASS_NAME, 'form-control.second')
        input2.send_keys("Ivanov")

        #  Поиск элемента по значению атрибута class
        input3 = browser.find_element(By.CLASS_NAME, 'form-control.third')
        input3.send_keys("Ivan@Ivanov.com")

        #  Поиск элемента с помощью правил на основе CSS
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        #  Ожидание загрузки страницы
        time.sleep(1)

        #  Поиск элемента содержащего текст по названию тега
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        #  Запись в переменную welcome_text текста из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration failed")

    def test_reg2(self):
        #  Присвоение адреса переменной link
        link = "http://suninjuly.github.io/registration2.html"

        #  Открытие адреса в Chrome
        browser = webdriver.Chrome()
        browser.get(link)

        #  Поиск элемента с помощью правил на основе CSS
        input1 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] > div[class="form-group first_class"] > input[class="form-control first"]')
        input1.send_keys("Ivan")

        #  Поиск элемента с помощью правил на основе CSS
        input2 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] > div[class="form-group second_class"] > input[class="form-control second"]')
        input2.send_keys("Ivanov")

        #  Поиск элемента с помощью правил на основе CSS
        input3 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] > div[class="form-group third_class"] > input[class="form-control third"]')
        input3.send_keys("Ivan@Ivanov.com")

        #  Поиск элемента с помощью правил на основе CSS
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        #  Ожидание загрузки страницы
        time.sleep(1)

        #  Поиск элемента содержащего текст по названию тега
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        #  Запись в переменную welcome_text текста из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration failed")


if __name__ == "__main__":
    unittest.main()
