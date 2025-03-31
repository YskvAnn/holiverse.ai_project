from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://b.metaforce.app/")

# нахожу и кликаю на кнопку + время на прокрутку
scroll_button = driver.find_element(By.CSS_SELECTOR, "button.menu-btn.btn-open")
scroll_button.click()
time.sleep(1)

text_h2 = driver.find_element(By.CSS_SELECTOR, "div.serviceModal-main-title")

# получаю текст элемента
element_text = text_h2.text
if element_text == "All Services":
    print("Заголовок совпадает с 'All Services'")
else:
    print(f"Заголовок не совпадает! Найдено: {element_text}")

driver.quit()
