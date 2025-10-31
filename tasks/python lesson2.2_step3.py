from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Открываем страницу
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects2.html")

try:
    # Находим элементы с числами
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    
    # Получаем текст чисел и преобразуем в целые числа
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    
    # Считаем сумму
    total = num1 + num2
    print(f"Число 1: {num1}, Число 2: {num2}, Сумма: {total}")
    
    # Находим выпадающий список
    dropdown = browser.find_element(By.ID, "dropdown")
    
    # Создаем объект Select для работы с выпадающим списком
    select = Select(dropdown)
    
    # Выбираем значение равное расчитанной сумме
    select.select_by_value(str(total))
    
    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # Даем время для отображения результата
    time.sleep(5)
    
    # Копируем число из алерта
    alert = browser.switch_to.alert
    result = alert.text
    print(f"Результат: {result}")
    alert.accept()
    
finally:
    # Закрываем браузер
    time.sleep(2)
    browser.quit()