from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up WebDriver
# Load environment variables from .env
load_dotenv()

driver_path = os.getenv("CHROMEDRIVER_PATH")
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://web.whatsapp.com")

input("Scan the QR code and press Enter to continue...")

contact_name = "Adam Caine"
message = "Answer"
interval = 0.5

# Wait for search box and open chat
search_box = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"))
)
search_box.click()
search_box.send_keys(contact_name)
search_box.send_keys(Keys.ENTER)

time.sleep(2)

# This loop targets the correct chat input using the specific div with aria-label "Type a message"
while True:
    try:
        msg_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((
                By.XPATH,
                "//div[@aria-label='Type a message'][@role='textbox'][@contenteditable='true']"
            ))
        )
        msg_box.click()
        msg_box.send_keys(message)
        msg_box.send_keys(Keys.ENTER)
        print("Message sent!")
        time.sleep(interval)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
