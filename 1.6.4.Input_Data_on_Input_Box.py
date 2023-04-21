# Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium.
# Если всё сделано правильно, то вы увидите окно с проверочным кодом.
# Это число вам нужно ввести в качестве ответа в этой задаче.


#  Импорт библиотек необходимых для работы программы
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#  Присвоение адреса переменной link
link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    #  Открытие адреса в Chrome
    browser = webdriver.Chrome()
    browser.get(link)

    #  Поиск по названию тега элемента: самый первый элемент с тегом input на странице
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")

    #  Поиск элемента по значению атрибута name
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")

    #  Поиск элемента по значению атрибута class
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")  # Вместо пробела ставим точку
    input3.send_keys("Smolensk")

    #  Поиск элемента по значению уникального атрибута id
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    #  Поиск элемента с помощью правил на основе CSS
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
