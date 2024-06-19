from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

class Screenshot:
    def take_screenshot(url: str) -> str:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in headless mode
        chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration

        # Set up the Chrome driver
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    
        try:
            # Open the URL

            driver.get('https://' + url)
            print('https://'+ url)
            # Wait for the page to load
            time.sleep(2)
            driver.maximize_window()
            time.sleep(1)  # Give the window time to maximize
            
            # Take the screenshot
            screenshot = driver.get_screenshot_as_png()
            if not os.path.exists("/tmp"):
                os.makedirs("/tmp")
            # Save the screenshot to a file
            file_path = f"/tmp/{url.replace('/', '_')}.png"
            with open(file_path, "wb") as f:
                f.write(screenshot)
    
        finally:
            # Close the driver
            driver.quit()
            
        return file_path