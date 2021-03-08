from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestFavicon(WebTestBase):

    def test_favicon(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        driver.find_element(By.XPATH, "//link[@rel='icon']")
