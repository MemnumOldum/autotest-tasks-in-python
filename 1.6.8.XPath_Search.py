# На этот раз воспользуемся возможностью искать элементы по XPath.
#
# На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3,
# при этом в нее добавилась куча одинаковых кнопок отправки. Но сработает только кнопка с текстом "Submit", и
# наша задача нажать в коде именно на неё.
#
# Ваши шаги:
#
# В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
# Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit. XPath можете формулировать
# как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
# Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
# Запустите ваш код.
# Если вы подобрали правильный селектор и все прошло хорошо, то вы получите код, который нужно отправить в качестве
# ответа на это задание.


#  Импорт библиотек необходимых для работы программы
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#  Присвоение адреса переменной link
link = "http://suninjuly.github.io/find_xpath_form"

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

    #  Поиск элемента с помощью XPath
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

