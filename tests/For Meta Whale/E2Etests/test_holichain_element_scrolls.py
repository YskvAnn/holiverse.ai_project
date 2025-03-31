from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://b.metaforce.app/")

# нахожу и кликаю на кнопку + время на прокрутку
scroll_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/ul/li[5]/a")
scroll_button.click()
time.sleep(5)

# h2
target_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/section[5]/div[1]/div[2]/div/h2")

current_scroll_position = driver.execute_script("return window.scrollY") # получаю текущую позицию страницы
element_position = target_element.location['y']

driver.execute_script("arguments[0].scrollIntoView();", target_element)
time.sleep(5)

# проверяю, что текущая позиция окна рядом с искомым элементов
element_position = driver.execute_script("return window.scrollY")

# проверяю, что позиция после прокрутки изменилась и стала соответствовать целевому элементу
assert abs(element_position - element_position) < 10, f"Ожидаемая прокрутка не произошла! Позиция: {element_position}, Ожидаемая: {element_position}"

print("Тест пройден успешно!")
driver.quit()
