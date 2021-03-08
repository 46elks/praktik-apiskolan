from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestOpenGraph(WebTestBase):

    def test_open_graph(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        driver.find_element(By.XPATH, "//meta[@property='og:title']")
        driver.find_element(By.XPATH, "//meta[@property='og:type']")
        driver.find_element(By.XPATH, "//meta[@property='og:url']")
        driver.find_element(By.XPATH, "//meta[@property='og:description']")
