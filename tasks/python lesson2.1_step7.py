from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Открываем страницу
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

try:
    # Находим элемент-картинку с сундуком
    treasure_img = browser.find_element(By.ID, "treasure")
    
    # Берем значение атрибута valuex
    x_value = treasure_img.get_attribute("valuex")
    print(f"Найдено значение x: {x_value}")
    
    # Вычисляем математическую функцию
    y = calc(x_value)
    print(f"Вычисленное значение y: {y}")
    
    # Вводим ответ в текстовое поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    
    # Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    # Выбираем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    
    # Нажимаем на кнопку "Submit"
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