from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
import time
# Получаем путь к ChromeDriver с помощью WebDriverManager
driver_path = ChromeDriverManager().install()

# Создаем объект Service
service = Service(driver_path)

# Инициализируем WebDriver с использованием Service
driver = webdriver.Chrome(service=service)

try:
    # Открытие страницы
    driver.get('https://b.metaforce.app/Home')
    time.sleep(3)

    # Нахождение элемента и клик по нему
    element = driver.find_element(By.CLASS_NAME, 'news__page-container')

    # Ожидание, чтобы страница успела обновиться (по желанию)
    time.sleep(2)

    # Получение текста элемента после клика
    element_text = driver.find_element(By.XPATH, 'news__page-container').text

    # Сравнение текста с ожидаемым
    expected_text = ('News and events '
                     'All News')
    assert element_text == expected_text, f"Тексты не совпадают! Получено: {element_text}, ожидается: {expected_text}"

    print("Тест пройден успешно!")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()