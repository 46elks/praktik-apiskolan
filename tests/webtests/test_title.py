from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestTitle(WebTestBase):
    
    def test_title(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Asserts if specific text is found in page title
        self.assertIn("APIskolan", driver.title)
