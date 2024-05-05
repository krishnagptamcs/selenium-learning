from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Importing By class
from selenium.webdriver.common.keys import Keys  # Importing By class

path = "C:/Users/krishna/OneDrive/Desktop/chromedriver-win64/chromedriver.exe"

s = Service(path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com")

# Find the input element on Google's search page and send keys
box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
box.send_keys("House of Dragon")
box.send_keys(Keys.ENTER)
