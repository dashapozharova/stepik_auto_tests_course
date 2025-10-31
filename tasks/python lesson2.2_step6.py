from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Открываем страницу
browser = webdriver.Chrome()
browser.get("https://SunInJuly.github.io/execute_script.html")

try:
    # Считываем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print(f"Найдено значение x: {x}")
    print(f"Вычисленное значение y: {y}")
    
    # Вводим ответ в текстовое поле
    answer_field = browser.find_element(By.ID, "answer")
    
    # Проскроллить страницу так, чтобы текстовое поле было видно
    browser.execute_script("arguments[0].scrollIntoView(true);", answer_field)
    
    # Вводим ответ
    answer_field.send_keys(y)
    
    # Выбираем checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    # Переключаем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    
    # Убеждаемся, что radiobutton виден (прокручиваем к нему)
    browser.execute_script("arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    
    # Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    
    # Прокручиваем к кнопке и нажимаем
    browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
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