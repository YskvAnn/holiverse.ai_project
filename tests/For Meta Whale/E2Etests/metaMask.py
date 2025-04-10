from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Путь к распакованному расширению MetaMask
metamask_path = "/Users/annyaskova/Downloads/metamask-chrome-12.15.2"

# Создаем опции Chrome
options = Options()
options.add_argument(f"--load-extension={metamask_path}")

# Создаем драйвер
driver = webdriver.Chrome(options=options)

# Ждём загрузку расширения
time.sleep(5)

# Открываем сайт с Web3 / MetaMask авторизацией
driver.get("https://b.metaforce.app/Home")



# Здесь нужно будет:
# 1. Переключиться на окно MetaMask (всплывающее окно)
# 2. Подтвердить подключение кошелька
# 3. Вернуться на сайт

# ... Здесь можно использовать driver.window_handles, driver.switch_to, .click() и т.д.
