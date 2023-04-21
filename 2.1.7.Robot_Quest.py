# Ваша программа должна:
#
# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".


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
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #  Поиск элемента с помощью правил на основе CSS
    #  Присвоение значения атрибута valuex - переменной x
    #  Присвоение результата вычисление математической функции от х - переменной y
    x_element = browser.find_element(By.CSS_SELECTOR, 'img[id=treasure]')
    x = x_element.get_attribute("valuex")
    y = calc(x)

    #  Поиск элемента с помощью правил на основе CSS, отправка результатов вычислений
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[id=answer]')
    input1.send_keys(y)

    #  Поиск чекбокса "I'm the robot" с помощью правил на основе CSS и нажатие на него
    checkbox1 = browser.find_element(By.CSS_SELECTOR, 'input[id=robotCheckbox]')
    checkbox1.click()

    #  Поиск радиобаттон "Robots rule!" с помощью правил на основе CSS и нажатие на него
    radio1 = browser.find_element(By.CSS_SELECTOR, 'input[id=robotsRule]')
    radio1.click()

    #  Поиск элемента с помощью правил на основе CSS
    button1 = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    button1.click()


finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
