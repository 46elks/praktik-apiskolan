from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
import requests

class TestHeader(WebTestBase):

    def test_link_names(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Find name by class
        navbar_names = driver.find_element(By.CLASS_NAME, "navbar-main").text
        # Search for text in navbar
        self.assertIn("Om oss", navbar_names)
        self.assertIn("Kontakt", navbar_names)
