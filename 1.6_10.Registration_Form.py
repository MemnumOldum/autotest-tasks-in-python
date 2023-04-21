# Вам дана страница с формой регистрации. Проверьте, что можно зарегистрироваться на сайте, заполнив
# только обязательные поля, отмеченные символом *: First name, last name, email. Текст для полей может быть любым.
# Успешность регистрации проверяется сравнением ожидаемого текста "Congratulations! You have successfully registered!"
# с текстом на странице, которая открывается после регистрации. Для сравнения воспользуемся
# стандартной конструкцией assert из языка Python.


#  Импорт библиотек необходимых для работы программы
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#  Присвоение адреса переменной link
link = "http://suninjuly.github.io/registration1.html"

try:
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

    #  Проверка с помощью assert, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
