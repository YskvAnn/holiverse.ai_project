from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()


try:

    driver.get("https://b.metaforce.app/")
    time.sleep(3)

# нахожу и кликаю элемент
    product_item = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/section[4]/div[2]/div[1]/div/div[2]")
    driver.execute_script("arguments[0].click();", product_item)
    time.sleep(5)

    # получаю список всех окон и переключаюсь на новое окно
    windows = driver.window_handles
    driver.switch_to.window(windows[1])

    # получаю URL нового окна и сравниваю с ожидаемым
    current_url = driver.current_url
    if current_url == "https://w-dex.ai/swap":
        print("URL соответствует ожидаемому")
    else:
        print("URL не соответствует ожидаемому")
finally: driver.quit()