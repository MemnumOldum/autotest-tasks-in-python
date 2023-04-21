# Сценарий для реализации выглядит так:
#
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ


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
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск элемента с помощью правил на основе CSS
    button1 = browser.find_element(By.CSS_SELECTOR, 'button[class="trollface btn btn-primary"]')
    button1.click()

    #  Присваиваем переменной вторую вкладку из списка всех вкладок(зная что сейчас всего две и вторая это новая)
    #  Переключаемся на вкладку из переменной
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
