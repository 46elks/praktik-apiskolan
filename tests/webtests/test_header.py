from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
import requests

class TestHeader(WebTestBase):

    def test_link_names(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Finds all text in navbar
        navbar_names = driver.find_element(By.ID, "mainNav").text.lower()

        # Asserts if specific text is found in navbar
        self.assertIn("om oss", navbar_names)
        self.assertIn("kontakt", navbar_names)

    def test_logo_link(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        navbar = driver.find_element(By.ID, "mainNav")

        # Attempts to find navbar-brand class in navbar (navbar logo)
        navbar.find_element(By.CLASS_NAME, "navbar-brand")
