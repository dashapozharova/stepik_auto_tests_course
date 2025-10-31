from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    
    # Находим все текстовые поля по тегу input
    elements = browser.find_elements(By.TAG_NAME, "input")
    
    # Заполняем каждое поле коротким текстом
    for element in elements:
        element.send_keys("Ответ")
    
    # Нажимаем кнопку отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла