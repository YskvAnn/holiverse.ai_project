from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()  # Используйте нужный WebDriver для вашего браузера

# Открытие страницы
driver.get("https://b.metaforce.app/")  # Замените на ваш URL

# Устанавливаем явное ожидание
wait = WebDriverWait(driver, 10)

# Находим кнопку, по которой нужно кликнуть
button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.primary.mf-btn.mod-large.mod-border-radius-16.mod-width-216"))  # Замените на ваш локатор кнопки
)

# Кликаем по кнопке
button.click()

# Находим элемент, который должен появиться после клика
element_to_check = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "modal-list"))
)

# Проверяем, что элемент стал видимым
assert element_to_check.is_displayed(), "Элемент не отобразился после клика!"

print("Тест пройден успешно!")

# Закрытие браузера
driver.quit()

