from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

try:
    # Нажимаем на кнопку, которая открывает новую вкладку
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    
    # Переключаемся на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
    
    # Решаем капчу на новой вкладке
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
    
    # Выводим результат крупным шрифтом
    print("=" * 50)
    print(f"РЕЗУЛЬТАТ: {result}")
    print("=" * 50)
    print("СКОПИРУЙТЕ ЧИСЛО ВЫШЕ!")
    
    # Ждем, пока пользователь скопирует результат
    input("Нажмите Enter для закрытия браузера...")
    
    # Закрываем алерт
    alert.accept()
    
finally:
    browser.quit()