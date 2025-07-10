from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

# Step 1: Open a website
driver.get("https://facebook.com")

# Step 2: Wait for page to load (basic)
time.sleep(2)


# Wait and close
time.sleep(3)

