from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestHeader(WebTestBase):

    def test_link_names(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Finds all text in navbar and makes it lowercase
        navbar_names = driver.find_element(By.ID, "mainNav").text.lower()

        # Asserts if specific text is found in navbar
        self.assertIn("om oss", navbar_names)
        self.assertIn("kontakt", navbar_names)

    def test_logo_link(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        result = False

        # Attempts to find logo in navbar
        navbar = driver.find_element(By.ID, "mainNav")
        navbar_brand = navbar.find_element(By.CLASS_NAME, "navbar-brand")
        logo = navbar_brand.find_element(By.TAG_NAME, "img")

        # Checks if logo contains "src" attribute
        if logo.get_attribute("src") != None:
            result = True

        self.assertTrue(result)


