from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestFavicon(WebTestBase):

    def test_favicon(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        driver.find_element(By.XPATH, "//link[@rel='apple-touch-icon']")
        driver.find_element(By.XPATH, "//link[@rel='icon']")
        driver.find_element(By.XPATH, "//link[@rel='manifest']")
        driver.find_element(By.XPATH, "//link[@rel='mask-icon']")
        driver.find_element(By.XPATH, "//link[@rel='shortcut icon']")

        driver.find_element(By.XPATH, "//meta[@name='msapplication-TileColor']")
        driver.find_element(By.XPATH, "//meta[@name='msapplication-config']")
        driver.find_element(By.XPATH, "//meta[@name='theme-color']")
