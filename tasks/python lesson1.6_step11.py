from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Тест для первой страницы (должен работать)
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    
    # Заполняем обязательные поля с уникальными селекторами
    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    input1.send_keys("Dasha")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second") 
    input2.send_keys("Pozharova")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
    input3.send_keys("Perm")
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    print(f"Страница 1: {welcome_text}")
    
finally:
    time.sleep(5)
    browser.quit()

# Тест для второй страницы (должен падать с ошибкой)
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    
    # Те же селекторы, но на второй странице одно поле отсутствует
    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    input1.send_keys("Dasha")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
    input2.send_keys("Pozharova")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
    input3.send_keys("Perm")
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    print(f"Страница 2: {welcome_text}")
    
except Exception as e:
    print(f"Ожидаемая ошибка на странице 2: {e}")
    
finally:
    time.sleep(5)
    browser.quit()