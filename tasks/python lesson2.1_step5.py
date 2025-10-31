from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Открываем страницу
browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/math.html")

try:
    # Ждем загрузки страницы
    wait = WebDriverWait(browser, 10)
    
    # Считываем значение для переменной x - ищем элемент с числом
    x_element = wait.until(EC.presence_of_element_located((By.ID, "input_value")))
    x = x_element.text
    print(f"Найдено значение x: {x}")
    y = calc(x)
    print(f"Вычисленное значение y: {y}")
    
    # Вводим ответ в текстовое поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.clear()
    answer_field.send_keys(y)
    
    # Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    # Выбираем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    
    # Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # Даем время для отображения результата
    time.sleep(5)
    
    # Проверяем, есть ли alert
    try:
        alert = browser.switch_to.alert
        result = alert.text
        print(f"Результат: {result}")
        alert.accept()
    except:
        print("Alert не найден, проверяем результат на странице")
        # Можно добавить проверку других элементов на странице
        
finally:
    # Небольшая задержка перед закрытием
    time.sleep(2)
    # Закрываем браузер
    browser.quit()