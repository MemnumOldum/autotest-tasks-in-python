# Напишите код, который реализует следующий сценарий:
#
# Открыть страницу https://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"


#  Импорт библиотек необходимых для работы программы
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select  # Добавляем из библиотеки класс SELECT Для работы со списками


# Создание функции сложения чисел
def calc(x, y):
    return int(x) + int(y)


try:
    #  Присвоение адреса переменной link и его открытие в Chrome
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #  Поиск элемента с помощью правил на основе CSS. Находим первое число
    x_element = browser.find_element(By.CSS_SELECTOR, 'h2 > span[id=num1]')
    x = x_element.text

    #  Поиск элемента с помощью правил на основе CSS. Находим второе число
    y_element = browser.find_element(By.CSS_SELECTOR, 'h2 > span[id=num2]')
    y = y_element.text

    #  Считаем сумму чисел используя функцию сложения
    z = calc(x, y)

    # Ищем выпадающий список по названию тега
    # Выбраем в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))

    #  Поиск элемента с помощью правил на основе CSS
    button1 = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    button1.click()




finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
