# Ваша задача -- реализовать автотест со следующим набором действий:
#
# открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
# авторизоваться со своими логином и паролем
# дождаться того, что поп-апа с авторизацией больше нет
#
# Задание: параметризация тестов
# Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
# Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений.
# Ваша задача — реализовать автотест со следующим сценарием действий:
#
# открыть страницу
# авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
# ввести правильный ответ (поле перед вводом должно быть пустым)
# нажать кнопку "Отправить"
# дождаться фидбека о том, что ответ правильный
# проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
# Опциональный фидбек — это текст в черном поле, как показано на скриншоте:

# Правильным ответом на задачу в заданных шагах является число:
#
# import time
# import math
#
# answer = math.log(int(time.time()))
# Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:
#
# https://stepik.org/lesson/236895/step/1
# https://stepik.org/lesson/236896/step/1
# https://stepik.org/lesson/236897/step/1
# https://stepik.org/lesson/236898/step/1
# https://stepik.org/lesson/236899/step/1
# https://stepik.org/lesson/236903/step/1
# https://stepik.org/lesson/236904/step/1
# https://stepik.org/lesson/236905/step/1
#



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest


# Фикстура browser создающая WebDriver
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



# Создание декоратора для запуска теста с разными тестовыми данными
@pytest.mark.parametrize('page', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1', 'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1', 'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1', 'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_prm(browser, page):
    browser.get(page)
    #  Ожидание загрузки страницы
    browser.implicitly_wait(5)
    #  Нажатие кнопки Входа
    button1 = browser.find_element(By.CSS_SELECTOR, 'a[id="ember33"]')
    button1.click()
    #  Ожидание загрузки страницы
    browser.implicitly_wait(5)

    #  Заполнение данных логин\пароль
    input1 = browser.find_element(By.CSS_SELECTOR, 'div > input[id="id_login_email"]')
    input1.send_keys("актуальный на stepiк.org логин")
    input2 = browser.find_element(By.CSS_SELECTOR, 'div > input[id="id_login_password"]')
    input2.send_keys("пароль от ведённого выше логина")
    button2 = browser.find_element(By.CSS_SELECTOR, 'form > button[class="sign-form__btn button_with-loader "]')
    button2.click()

    #  Ввод ответа, подтверждение отправки, очистка текстового поля
    #  Ожидание обновления страницы
    time.sleep(5)
    input3 = browser.find_element(By.CSS_SELECTOR, "div[class='show-plugin'] > div[data-state='no_submission'] > textarea[placeholder='Напишите ваш ответ здесь...']")
    y = math.log(int(time.time()))
    input3.send_keys(y)
    #  Ожидание активации кнопки
    time.sleep(2)
    button3 = browser.find_element(By.CSS_SELECTOR, "div[class='attempt__inner'] > div[class='attempt__actions'] > button[class='submit-submission']")
    button3.click()
    time.sleep(2)
    answer = browser.find_element(By.CSS_SELECTOR, 'div[class="smart-hints ember-view lesson__hint"] > p[class="smart-hints__hint"]')
    #  Сохранение ответов отличающихся от 'Correct!' в file.txt
    if answer.text != 'Correct!':
        with open('file.txt', 'a') as file:
            file.write(answer.text)

    #  Ожидание добавления кнопки
    time.sleep(3)
    button4 = browser.find_element(By.CSS_SELECTOR, "div[class='attempt__inner'] > div[class='attempt__actions'] > button[class='again-btn white']")
    button4.click()
    time.sleep(5)
