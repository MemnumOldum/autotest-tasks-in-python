# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером,
# который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:
#
# Открыть страницу https://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
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
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #  Поиск элемента с помощью правил на основе CSS
    #  Присвоение содержимого текстового поля элемента - переменной x
    #  Присвоение результата вычисление математической функции от х - переменной y
    x_element = browser.find_element(By.CSS_SELECTOR, 'label > span[id="input_value"]')
    x = x_element.text
    y = calc(x)

    #  Поиск элемента с помощью правил на основе CSS, отправка результатов вычислений
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[id=answer]')
    input1.send_keys(y)

    #  Поиск чекбокса "I'm the robot" с помощью правил на основе CSS и нажатие на него
    checkbox1 = browser.find_element(By.CSS_SELECTOR, 'input[id=robotCheckbox]')
    checkbox1.click()

    #  Поиск радиобаттон "Robots rule!" с помощью правил на основе CSS,
    #  скроллинг страницы до открытия видимости элемента и нажатие на него
    radio1 = browser.find_element(By.CSS_SELECTOR, 'input[id=robotsRule]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio1)
    radio1.click()

    # Поиск элемента с помощью правил на основе CSS,
    #  скроллинг страницы до открытия видимости элемента и нажатие на него
    button1 = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()


finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
