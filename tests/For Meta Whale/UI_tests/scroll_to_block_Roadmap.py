from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://b.metaforce.app/")
driver.implicitly_wait(15)

# нахожу и кликаю на кнопку + время на прокрутку
scroll_button = driver.find_element(By.XPATH, "/html/body/div/div/div/header/ul/li[3]/a")
scroll_button.click()
time.sleep(2)

# h2
target_element = driver.find_element(By.XPATH, "//h2[text()='Roadmap']")

current_scroll_position = driver.execute_script("return window.scrollY") # получаю текущую позицию страницы
element_position = target_element.location['y']

driver.execute_script("arguments[0].scrollIntoView();", target_element)
time.sleep(1)

# проверяю, что текущая позиция окна рядом с искомым элементов
new_scroll_position = driver.execute_script("return window.scrollY")

# проверяю, что позиция после прокрутки изменилась и стала соответствовать целевому элементу
assert abs(new_scroll_position - element_position) < 10, f"Ожидаемая прокрутка не произошла! Позиция: {new_scroll_position}, Ожидаемая: {element_position}"

print("Тест пройден успешно!")

# Закрытие браузера
driver.quit()
