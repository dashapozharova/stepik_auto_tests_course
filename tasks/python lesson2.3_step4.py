from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

try:
    # Нажимаем на кнопку, которая вызывает confirm
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    
    # Принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    
    # Ждем загрузки новой страницы
    time.sleep(1)
    
    # Решаем капчу на новой странице
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ в текстовое поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    
    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # Получаем результат из алерта
    time.sleep(2)
    alert = browser.switch_to.alert
    result = alert.text
    print(f"Результат: {result}")
    alert.accept()
    
finally:
    time.sleep(2)
    browser.quit()