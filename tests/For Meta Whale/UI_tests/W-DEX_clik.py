from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка опций для Chrome
options = Options()
options.headless = False  # Если нужно скрыть браузер, установите True
options.add_argument("--start-maximized")  # Окно браузера будет максимизировано

# Запуск Chrome с помощью WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Открываем страницу
    driver.get("https://b.metaforce.app/")

    # Ожидаем появления элемента с классом landing-products__item
    product_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/section[4]/div[2]/div[1]/div/div[2]"))
    )

    # Если элемент не является ссылкой, используем JavaScript для клика
    driver.execute_script("arguments[0].click();", product_item)

    # Увеличим время ожидания до 30 секунд, чтобы подождать, пока URL изменится
    WebDriverWait(driver, 30).until(EC.url_contains("https://w-dex.ai/swap"))

    # Проверка, что URL страницы теперь начинается с https://w-dex.ai/swap
    current_url = driver.current_url
    print(f"Текущий URL: {current_url}")
    assert "https://w-dex.ai/swap" in current_url, f"Ошибка! Ожидался URL, начинающийся с 'https://w-dex.ai/swap', но открылся '{current_url}'"

    print("Тест пройден успешно! Перешли на правильную страницу.")

finally:
    # Закрыть браузер
    driver.quit()
