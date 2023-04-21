# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение


#  Импорт библиотек необходимых для работы программы
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math


# Создание математической функции от x
def calc(x1):
    return str(math.log(abs(12 * math.sin(int(x1)))))


try:
    #  Присвоение адреса переменной link и его открытие в Chrome
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #  Ожидание пока текстовое содержимое элемента примет значение равное 100
    #  Пока этого не случится программа не перейдёт к следующему шагу и не подтвердит аренду
    price = WebDriverWait(browser, 15).until(expected_conditions.text_to_be_present_in_element
                                             ((By.CSS_SELECTOR, 'div > h5[id="price"]'), '100'))

    # Поиск элемента с помощью правил на основе CSS
    button1 = browser.find_element(By.CSS_SELECTOR, 'div > button[id="book"]')
    button1.click()

    #  Поиск элемента с помощью правил на основе CSS
    #  Присвоение содержимого текстового поля элемента - переменной x
    #  Присвоение результата вычисление математической функции от х - переменной y
    x_element = browser.find_element(By.CSS_SELECTOR, 'label > span[id=input_value]')
    x = x_element.text
    y = calc(x)

    #  Поиск элемента с помощью правил на основе CSS, отправка результатов вычислений
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[id=answer]')
    input1.send_keys(y)

    #  Поиск элемента с помощью правил на основе CSS
    button2 = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    button2.click()

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
