from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Создаем временный текстовый файл для загрузки
file_content = "This is a test file for upload"
file_path = os.path.join(os.getcwd(), "test_file.txt")

# Записываем содержимое в файл
with open(file_path, "w") as file:
    file.write(file_content)

print(f"Создан файл для загрузки: {file_path}")

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

try:
    # Заполняем текстовые поля
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")
    
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Petrov")
    
    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@example.com")
    
    # Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)
    
    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # Получаем результат из алерта
    alert = browser.switch_to.alert
    result = alert.text
    print(f"Результат: {result}")
    alert.accept()
    
finally:
    browser.quit()
    # Удаляем временный файл (опционально)
    if os.path.exists(file_path):
        os.remove(file_path)
        print("Временный файл удален")