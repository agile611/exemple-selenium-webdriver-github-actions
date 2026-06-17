import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestYahoo(unittest.TestCase):
    """Test suite for Yahoo.com"""

    def setUp(self):
        """Set up the WebDriver before each test"""
        # Configure Chrome options
        chrome_options = Options()
        
        # Run in headless mode in CI/CD environments
        if os.getenv("CI") or os.getenv("GITHUB_ACTIONS"):
            chrome_options.add_argument("--headless")
        
        # Additional arguments for stability
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # Initialize WebDriver with webdriver-manager
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Close the WebDriver after each test"""
        self.driver.quit()

    def test_open_yahoo_homepage(self):
        """Test that Yahoo homepage opens successfully"""
        # Open Yahoo
        self.driver.get("https://www.yahoo.com")

        # Wait for the page title to be present
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Yahoo")
        )

        # Verify the page loaded
        self.assertIn("Yahoo", self.driver.title)

        # Print success message
        print(f"✓ Yahoo page loaded successfully. Title: {self.driver.title}")


if __name__ == "__main__":
    unittest.main()
