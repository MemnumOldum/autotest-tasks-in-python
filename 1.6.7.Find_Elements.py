# Задание: использование метода find_elements
# В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html). С помощью неё отдел маркетинга
# компании N захотел собрать подробную информацию о пользователях своего продукта. В награду за заполнение формы
# становится доступен код на скидку. Но маркетологи явно переусердствовали, добавив в форму 100 обязательных полей
# и ограничив время на ее заполнение. Теперь эта задача под силу только роботам
#
# Используйте WebDriver, метод find_elements, нужные локатор и его значение. Введите полученный код в качестве ответа к
# этой задаче.


#  Импорт библиотек необходимых для работы программы
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    #  Открытие адреса в Chrome
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    #  Метод find_elements, который в отличие от find_element
    #  вернёт список всех найденных элементов по заданному условию.
    #  Поиск по названию тега элементов: все элементы с тегом input на странице
    elements = browser.find_elements(By.TAG_NAME, "input")

    # в цикле for мы можем последовательно взять каждый элемент из найденного списка текстовых полей
    # и отправить произвольный текст в каждое поле.
    for element in elements:
        element.send_keys("Мой ответ")

    #  Поиск элемента с помощью правил на основе CSS
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
