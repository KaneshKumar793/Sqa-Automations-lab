
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/html/html_forms.asp")


elem_id = driver.find_element(By.ID, "fname")

print("Found by ID:", elem_id.get_attribute("placeholder"))

links = driver.find_elements(By.TAG_NAME, "a")

print("Total links:", len(links))


btn = driver.find_element(
    By.CSS_SELECTOR,
    'input[type="submit"]'
)

print("Button found:", btn.get_attribute("value"))

driver.quit()
