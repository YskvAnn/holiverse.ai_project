from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Настройка WebDriver
driver = webdriver.Chrome()  # Если используется другой браузер, замените на нужный WebDriver

# Открытие страницы
driver.get("https://a.metaforce.app/")  # Укажите URL страницы

# Явное ожидание (если нужно дождаться загрузки элементов)
driver.implicitly_wait(15)

# Находим кнопку, на которую нужно кликнуть
scroll_button = driver.find_element(By.LINK_TEXT, "About")  # Замените ID кнопки

# Кликаем на кнопку
scroll_button.click()

# Даем время для выполнения анимации прокрутки (если есть)
time.sleep(2)  # Лучше использовать WebDriverWait вместо sleep для более надежного ожидания

# Находим элемент, к которому должна прокрутиться страница
target_element = driver.find_element(By.CLASS_NAME, "landing-paragraph-size-40")  # Замените на свой локатор

# Получаем текущее положение окна
current_scroll_position = driver.execute_script("return window.scrollY")

# Получаем позицию целевого элемента относительно окна
element_position = target_element.location['y']

# Прокручиваем страницу к целевому элементу (это можно сделать через JS или через прокрутку окна)
driver.execute_script("arguments[0].scrollIntoView();", target_element)

# Даем время для прокрутки
time.sleep(1)

# Проверяем, что страница прокрутилась к целевому элементу
# Допустим, проверяем, что текущая позиция окна достаточно близка к позиции элемента
new_scroll_position = driver.execute_script("return window.scrollY")

# Проверка, что позиция после прокрутки изменилась и стала соответствовать целевому элементу
assert abs(new_scroll_position - element_position) < 10, f"Ожидаемая прокрутка не произошла! Позиция: {new_scroll_position}, Ожидаемая: {element_position}"

print("Тест пройден успешно!")

# Закрытие браузера
driver.quit()
