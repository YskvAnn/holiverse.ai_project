from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка Service для ChromeDriver
service = Service('/opt/homebrew/bin/chromedriver')  # Укажите путь к chromedriver

# Инициализация WebDriver с использованием Service
driver = webdriver.Chrome(service=service)

try:
    # Открытие страницы
    driver.get('https://b.metaforce.app/')

    # Явное ожидание загрузки страницы и кнопки
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.menu-btn.btn-open')))

    # Клик по кнопке menu-btn
    menu_button = driver.find_element(By.CSS_SELECTOR, 'button.menu-btn.btn-open')
    menu_button.click()

    # Ожидание появления элемента в меню
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#menuModal > div.serviceModal-content > div.content-lg > ul:nth-child(2) > li:nth-child(5) > div')))

    # Клик по кнопке serviceModal
    service_button = driver.find_element(By.CSS_SELECTOR, '#menuModal > div.serviceModal-content > div.content-lg > ul:nth-child(2) > li:nth-child(5) > div')
    service_button.click()

    # Ожидание изменения URL (используем url_contains, чтобы не зависеть от точного совпадения URL)
    WebDriverWait(driver, 20).until(EC.url_contains("dex.holiverse.ai/swap"))  # Проверка, что URL содержит подстроку "dex.holiverse.ai/swap"

    # Проверка текущего URL
    current_url = driver.current_url
    print(f"Текущий URL: {current_url}")
    assert "dex.holiverse.ai/swap" in current_url, f'Expected URL to contain "dex.holiverse.ai/swap", but got {current_url}'

    print("Тест пройден успешно!")

except Exception as e:
    print(f"Тест не пройден: {e}")

finally:
    # Закрытие браузера
    driver.quit()
