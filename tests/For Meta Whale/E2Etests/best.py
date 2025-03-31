from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://a.metaforce.app/")
wait = WebDriverWait(driver, 10)
scroll_button = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Roadmap")))

scroll_button.click()

target_element = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "landing-container"))
)

driver.execute_script("arguments[0].scrollIntoView();", target_element)

wait.until(lambda driver: driver.execute_script("return window.scrollY") != 0)

new_scroll_position = driver.execute_script("return window.scrollY")


element_position = target_element.location['y']
window_height = driver.execute_script("return window.innerHeight")


assert element_position >= new_scroll_position and element_position <= new_scroll_position + window_height, \
    f"Ожидаемая прокрутка не произошла! Позиция: {new_scroll_position}, Элемент: {element_position}, Высота окна: {window_height}"

print("Тест пройден успешно!")
driver.quit()
