from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
class Screenhshot:
    def take_screenshot(url):
        # Set up Chrome options
        chrome_options = Options()
    
        # Set up the Chrome driver
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    
        try:
            # Open the URL
            driver.get(url)
        
            # Wait for the page to load
            time.sleep(2)
            driver.maximize_window()
            time.sleep(1)  # Give the window time to maximize
            # Take the screenshot
            screenshot = driver.get_screenshot_as_png()
    
        finally:
            # Close the driver
            driver.quit()
        return screenshot
