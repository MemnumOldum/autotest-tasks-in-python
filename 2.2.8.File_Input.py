# Напишите скрипт, который будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"


#  Импорт библиотек необходимых для работы программы
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    #  Присвоение адреса переменной link и его открытие в Chrome
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск элемента с помощью правил на основе CSS
    input1 = browser.find_element(By.CSS_SELECTOR, 'div[class="form-group"] > input[name="firstname"]')
    input1.send_keys("Ivan")

    # Поиск элемента с помощью правил на основе CSS
    input2 = browser.find_element(By.CSS_SELECTOR, 'div[class="form-group"] > input[name="lastname"]')
    input2.send_keys("Ivanov")

    # Поиск элемента с помощью правил на основе CSS
    input3 = browser.find_element(By.CSS_SELECTOR, 'div[class="form-group"] > input[name="email"]')
    input3.send_keys("Ivan@Ivanov.com")

    #   Поиск элемента отправки файла с помощью правил на основе CSS
    #   Получение пути к директории текущего исполняемого файла(отправляемый файл лежит в этой же директории)
    #   Добавление к этому пути имени файла
    #   Прикрепление файла
    element = browser.find_element(By.CSS_SELECTOR, 'form[action="#"] > input[id=file]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)

    # Поиск элемента с помощью правил на основе CSS
    button1 = browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    button1.click()


finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
