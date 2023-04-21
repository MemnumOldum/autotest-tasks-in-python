# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом

#  Импорт библиотек необходимых для работы программы
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# Создание математической функции от x
def calc(x1):
    return str(math.log(abs(12 * math.sin(int(x1)))))


try:
    #  Присвоение адреса переменной link и его открытие в Chrome
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск элемента с помощью правил на основе CSS
    button1 = browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    button1.click()

    #  Переключение на окно confirm и принятие его
    confirm = browser.switch_to.alert
    confirm.accept()

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
