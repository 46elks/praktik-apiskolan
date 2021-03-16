from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestContentPage(WebTestBase):

    def test_image(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        
        # Attempts to navigate to content page
        navbar_nav = driver.find_element(By.CLASS_NAME, "navbar-nav")
        content_button = navbar_nav.find_element(By.XPATH, "//a[@href='content.html']")
        content_button.click()
        
        result = False

        # Attempts to find photo in content page
        photo = driver.find_element(By.TAG_NAME, "img")

        # Checks if image contains "src" attribute
        if photo.get_attribute("src") != None:
            result = True

        self.assertTrue(result)

def test_quiz(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        
        # Attempts to navigate to content page
        navbar_nav = driver.find_element(By.CLASS_NAME, "navbar-nav")
        content_button = navbar_nav.find_element(By.XPATH, "//a[@href='content.html']")
        content_button.click()

        quiz = driver.find_element(By.ID, "quiz")

