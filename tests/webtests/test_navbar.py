from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestNavbar(WebTestBase):
    
    def test_test(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)