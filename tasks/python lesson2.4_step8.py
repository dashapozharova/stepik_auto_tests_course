from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # Ждем, когда цена дома уменьшится до $100 (ожидание не меньше 12 секунд)
    wait = WebDriverWait(browser, 15)  # Устанавливаем ожидание 15 секунд
    
    # Ожидаем, когда текст в элементе с id="price" станет равным "$100"
    price_element = wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    # Когда цена стала $100, нажимаем на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    
    # Решаем математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ в текстовое поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    
    # Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    
    # Получаем результат из алерта
    alert = browser.switch_to.alert
    result = alert.text
    
    # Выводим результат
    print("=" * 50)
    print(f"РЕЗУЛЬТАТ: {result}")
    print("=" * 50)
    
    # Ждем, пока пользователь скопирует результат
    input("Скопируйте число и нажмите Enter для закрытия...")
    
    # Закрываем алерт
    alert.accept()
    
finally:
    browser.quit()