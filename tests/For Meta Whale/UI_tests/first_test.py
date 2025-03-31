from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://b.metaforce.app/")

print(driver.title)
driver.quit()
