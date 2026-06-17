import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestYahooSearch(unittest.TestCase):
    """Test suite for Yahoo search functionality"""

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

    def wait_for_element_clickable(self, element, timeout=10):
        """Wait for an element to be clickable"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.element_to_be_clickable(element))

    def test_yahoo_search_hawaiian_pizza(self):
        """Test Yahoo search functionality for 'pizza hawaiana'"""
        # Open Yahoo
        self.driver.get("https://www.yahoo.com/")
        
        # Store original window handle
        original_window = self.driver.current_window_handle
        
        try:
            # Find and click the accept/agree button
            accept_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@value='agree']"))
            )
            accept_button.click()
            print("✓ Accept button clicked")
        except Exception as e:
            print(f"⚠ Accept button not found (may have already been accepted): {e}")
        
        # Find the search box
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@type='search']"))
        )
        
        # Click on search box, clear it, and enter search term
        search_box.click()
        search_box.clear()
        search_box.send_keys("hawaiian pizza")
        print("✓ Search term entered: 'hawaiian pizza'")
        
        # Submit the search
        search_box.submit()
        
        # Wait for new window to open (up to 20 seconds)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.number_of_windows_to_be(2))
        print("✓ New window opened")
        
        # Find and switch to the new window
        new_window = None
        for handle in self.driver.window_handles:
            if handle != original_window:
                new_window = handle
                break
        
        if new_window:
            self.driver.switch_to.window(new_window)
            print(f"✓ Switched to new window: {new_window}")
        else:
            self.fail("New window handle not found")
        
        # Wait for and verify search results are displayed
        try:
            search_results = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "results"))
            )
            
            # Assert that results are displayed
            self.assertTrue(search_results.is_displayed(), "Search results should be displayed")
            print("✓ Search results displayed successfully")
            
        except Exception as e:
            self.fail(f"Search results element not found: {e}")
        
        # Wait 5 seconds to observe the results
        time.sleep(5)
        print("✓ Test completed successfully")


if __name__ == "__main__":
    unittest.main()
