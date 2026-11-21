
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print("Page Title:", driver.title)
print("Current URL:", driver.current_url)

driver.quit()
