from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://b.metaforce.app/")
time.sleep(5)
# нахожу и кликаю на кнопку + время на прокрутку
scroll_button = driver.find_element(By.XPATH, "/html/body/div/div/div/header/div[2]/button[1]")
scroll_button.click()
time.sleep(5)

text_h2 = driver.find_element(By.CSS_SELECTOR, "div.modal-title")

# получаю текст элемента
element_text = text_h2.text
if element_text == "Connect wallet":
    print("Заголовок совпадает с 'Connect wallet'")
else:
    print(f"Заголовок не совпадает! Найдено: {element_text}")

driver.quit()
