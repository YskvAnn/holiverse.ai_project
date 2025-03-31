from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Получаем путь к ChromeDriver с помощью WebDriverManager
driver_path = ChromeDriverManager().install()

# Создаем объект Service
service = Service(driver_path)

# Инициализируем WebDriver с использованием Service
driver = webdriver.Chrome(service=service)

# Открываем сайт
driver.get("https://b.metaforce.app/")

# Выводим заголовок страницы
print(driver.title)

# Закрываем браузер
driver.quit()
