# На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:
#
# Добавьте в самый верх своего кода import math
# Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
# Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
# str(math.ceil(math.pow(math.pi, math.e)*10000))
#
# Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
#
# Заполните скриптом форму так же как вы делали в предыдущем шаге урока
#
# После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание
# Важно! Поиск по тексту ссылки бывает очень удобным, так часто тексты меняются реже, чем атрибуты элементов.
# Но лучше избегать такого метода поиска. Например, если приложение имеет несколько языков интерфейса,
# ваши тесты будут проходить только с определенным языком интерфейса. Применяйте этот метод с осторожностью и
# помните про возможные ограничения.


#  Импорт библиотек необходимых для работы программы
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

#  Присвоение адреса переменной link
link = "http://suninjuly.github.io/find_link_text"

try:
    #  Открытие адреса в Chrome
    browser = webdriver.Chrome()
    browser.get(link)

    #  Поиск ссылки на странице по полному совпадению
    button = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    button.click()

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
