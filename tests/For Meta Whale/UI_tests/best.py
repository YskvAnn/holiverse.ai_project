from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка WebDriver
driver = webdriver.Chrome()  # Если используется другой браузер, замените на нужный WebDriver

# Открытие страницы
driver.get("https://a.metaforce.app/")  # Укажите URL страницы

# Устанавливаем явное ожидание для элементов
wait = WebDriverWait(driver, 10)

# Находим кнопку "About" с использованием явного ожидания
scroll_button = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Roadmap"))
)

# Кликаем на кнопку
scroll_button.click()

# Ожидаем, пока целевой элемент станет доступным на странице (можно ожидать его появление или видимость)
target_element = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "landing-container"))
)

# Прокручиваем страницу к целевому элементу с использованием JavaScript
driver.execute_script("arguments[0].scrollIntoView();", target_element)

# Явное ожидание, пока прокрутка не завершится (можно установить небольшое время задержки)
wait.until(lambda driver: driver.execute_script("return window.scrollY") != 0)  # Прокрутка должна измениться

# Получаем текущую позицию прокрутки после того, как страница прокручена
new_scroll_position = driver.execute_script("return window.scrollY")

# Проверяем, что целевой элемент в пределах видимой области
element_position = target_element.location['y']
window_height = driver.execute_script("return window.innerHeight")

# Проверка, что элемент видим в области окна (не выходит за пределы видимости)
assert element_position >= new_scroll_position and element_position <= new_scroll_position + window_height, \
    f"Ожидаемая прокрутка не произошла! Позиция: {new_scroll_position}, Элемент: {element_position}, Высота окна: {window_height}"

print("Тест пройден успешно!")

# Закрытие браузера
driver.quit()
