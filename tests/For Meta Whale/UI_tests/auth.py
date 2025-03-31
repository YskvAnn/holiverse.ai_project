from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False


service = Service(ChromeDriverManager().install())
remember_token = '$2y$10$EYDUjmAK6AqmzLGPjOwEIO23GUAmqyz/ueHkSc8TgtqQb1lJj.ADi'

headers = {
    'Authorization': f'Bearer {remember_token}'
}

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://meta-whale.com/Home')

time.sleep(10)
try:

    title = driver.find_element(By.TAG_NAME, 'h1').text
    print(f"Заголовок на странице: {title}")
except Exception as e:
    print("Ошибка при поиске элемента на странице:", e)

driver.quit()
