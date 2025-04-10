from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

options = Options()
options.headless = False


service = Service(ChromeDriverManager().install())
remember_token = '$2y$10$AaNbRxiZDY58kfL6tcs8LukTtOdZgJTQviGiVyZuRRv8yhu2KK9NW'

headers = {
    'Authorization': f'Bearer {remember_token}'
}
data = {"force_remember_token": remember_token}

with open("local_storage.json", "w") as f:
    json.dump(data, f)

with open("local_storage.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)


driver = webdriver.Chrome(service=service, options=options)
driver.get('https://b.metaforce.app/Home')

time.sleep(10)
try:

    title = driver.find_element(By.TAG_NAME, 'h1').text
    print(f"Заголовок на странице: {title}")
except Exception as e:
    print("Ошибка при поиске элемента на странице:", e)

driver.quit()
