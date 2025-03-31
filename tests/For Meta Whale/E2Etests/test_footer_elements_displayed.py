from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://b.metaforce.app/")
time.sleep(5)


# нахожу все элементы футера
footer = driver.find_element(By.CSS_SELECTOR, "div.footer")

footer_links = footer.find_elements(By.TAG_NAME, "p")  # Находим все ссылки в футтере

# Проверяем, что в футтере есть необходимые элементы
required_elements = ["W-DEX", "T&S" ,"Dashboard", "Discover","My profile","My team","Support","Events","Reviews","Smart Contracts","About","News" ]

for element in required_elements:
        found = False
        for link in footer_links:
            if link.text == element:
                found = True
                break
assert found, f"Элемент '{element}' не найден в футтере!"
print("Все элементы футтера на месте!")

#Закрытие браузера
driver.quit()

