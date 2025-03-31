from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
import time

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:

    driver.get('https://b.metaforce.app/Home')
    time.sleep(3)
    element = driver.find_element(By.CLASS_NAME, 'news__page-container')
    time.sleep(2)

    # получаю текст элемента после клика
    element_text = driver.find_element(By.XPATH, 'news__page-container').text

    # сравниваю текст с ожидаемым
    expected_text = ('News and events '
                     'All News')
    assert element_text == expected_text, f"Тексты не совпадают! Получено: {element_text}, ожидается: {expected_text}"

    print("Тест пройден успешно!")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()