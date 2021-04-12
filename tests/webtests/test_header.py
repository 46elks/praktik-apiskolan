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

    def test_button(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Attempts to navigate to content page with button
        navbar = driver.find_element(By.ID, "mainNav")
        button = navbar.find_element(By.XPATH, "//a[@href='content.html']")
        button.click()

        # Asserts if the wrapper of content page is found
        self.assertIn("contentWrapper", driver.page_source)

    def test_logo_image(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Attempts to find logo in navbar
        navbar = driver.find_element(By.ID, "mainNav")
        navbar_brand = navbar.find_element(By.CLASS_NAME, "navbar-brand")
        logo = navbar_brand.find_element(By.TAG_NAME, "img").get_attribute("src")

        self.assertIn("logo", logo)
        self.assertIn(".svg", logo)

