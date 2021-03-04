from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
import requests

class TestHeader(WebTestBase):

    def test_link_names(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Find all text in navbar
        navbar_names = driver.find_element(By.ID, "mainNav").text

        # Assert if specific text is in navbar
        self.assertIn("Om oss", navbar_names)
        self.assertIn("Kontakt", navbar_names)
