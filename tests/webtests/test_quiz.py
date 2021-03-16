from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestQuiz(WebTestBase):
    
    def test_quiz(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
