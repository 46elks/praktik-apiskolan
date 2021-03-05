from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestFooter(WebTestBase):

    def test_exists(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Attempts to find footer element on page
        driver.find_element(By.TAG_NAME, "footer")
