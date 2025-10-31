import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Вычисляем зашифрованный текст ссылки
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(f"Ищем ссылку с текстом: {link_text}")

try:
    browser = webdriver.Chrome()
    
    # Открываем страницу с ссылками
    browser.get("http://suninjuly.github.io/find_link_text")
    
    # Находим ссылку по зашифрованному тексту
    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()
    
    # Заполняем форму на новой странице
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    
    # Отправляем форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Копируем код из алерта
    time.sleep(10)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Код из алерта: {alert_text}")
    alert.accept()
    browser.quit()