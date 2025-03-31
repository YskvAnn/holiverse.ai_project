from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Опционально для автоматической установки драйвера
import time
# Устанавливаем опции для Chrome
options = Options()
options.headless = False  # Запускать в фоновом режиме (True) или с графическим интерфейсом (False)

# Используем Service для указания пути к ChromeDriver
service = Service(ChromeDriverManager().install())  # или просто укажите свой путь к ChromeDriver

# Токен для аутентификации
remember_token = '$2y$10$EYDUjmAK6AqmzLGPjOwEIO23GUAmqyz/ueHkSc8TgtqQb1lJj.ADi'

# Настроим заголовки для запроса
headers = {
    'Authorization': f'Bearer {remember_token}'
}
# Инициализация драйвера с помощью Service
driver = webdriver.Chrome(service=service, options=options)

# Открываем страницу с использованием токена в заголовках
driver.get('https://meta-whale.com/Home')

time.sleep(10)
# Пример проверки, что страница загрузилась
try:
    # Здесь проверим, что на странице есть элемент, например, заголовок
    title = driver.find_element(By.TAG_NAME, 'h1').text
    print(f"Заголовок на странице: {title}")
except Exception as e:
    print("Ошибка при поиске элемента на странице:", e)

# Закрываем драйвер
driver.quit()
