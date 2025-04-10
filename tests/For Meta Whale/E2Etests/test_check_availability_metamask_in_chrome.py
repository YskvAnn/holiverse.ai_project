from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://b.metaforce.app/")  # или твоя страница

is_metamask_installed = driver.execute_script("""
    return (typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask);
""")

print("MetaMask installed:", is_metamask_installed)
driver.quit()

