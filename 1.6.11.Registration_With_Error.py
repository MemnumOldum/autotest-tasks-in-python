# У нас уже есть простой тест из предыдущего шага, который проверяет возможность зарегистрироваться на сайте.
# Однако разработчики решили немного поменять верстку страницы, чтобы она выглядела более современной.
# Обновленная страница доступна по другой ссылке. К сожалению, в процессе изменений они
# случайно внесли баг в форму регистрации.

# Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку.
# Если ваш тест упал с ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы
# и смогли обнаружить баг, который создали разработчики. Это хорошо! Значит, ваши тесты сработали как надо.
# Пугаться не стоит, здесь ошибка в приложении которое вы тестируете, а не в вашем тесте.
#
# Если же ваш тест прошел успешно, то это означает, что тест пропустил серьезный баг.
# В этом случае попробуйте поменять селекторы, сделав их уникальными. После изменения убедитесь,
# что ваш тест исправно проходит в старой версии страницы.
#
# Чтобы получить максимальное количество баллов, прежде чем отправлять решение на рецензию,
# самостоятельно убедитесь в том что:
#
# 1. Тест успешно проходит на странице http://suninjuly.github.io/registration1.html
# 2. Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html
# 3. Используемые селекторы должны быть уникальны


#  Импорт библиотек необходимых для работы программы
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#  Присвоение адреса переменной link
link = "http://suninjuly.github.io/registration2.html"

try:
    #  Открытие адреса в Chrome
    browser = webdriver.Chrome()
    browser.get(link)

    #  Поиск элемента с помощью правил на основе CSS
    input1 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] > div[class="form-group first_class"] > '
                                                   'input[class="form-control first"]')
    input1.send_keys("Ivan")

    #  Поиск элемента с помощью правил на основе CSS
    input2 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] > div[class="form-group second_class"] > '
                                                   'input[class="form-control second"]')
    input2.send_keys("Ivanov")

    #  Поиск элемента с помощью правил на основе CSS
    input3 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] > div[class="form-group third_class"] > '
                                                   'input[class="form-control third"]')
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
