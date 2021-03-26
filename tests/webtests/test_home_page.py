from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestHomePage(WebTestBase):
    
    def test_button(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Attempts to navigate to content page with button
        masthead = driver.find_element(By.ID, "indexMasthead")
        masthead_button = masthead.find_element(By.XPATH, "//a[@href='content.html']")
        masthead_button.click()

        # Asserts if the wrapper of content page is found
        self.assertIn("contentWrapper", driver.page_source)

    def test_text(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Finds the tags for masthead
        masthead = driver.find_element(By.ID, "indexMasthead")
        masthead_h1 = masthead.find_element(By.TAG_NAME, "h1")
        masthead_h2 = masthead.find_element(By.TAG_NAME, "h2")

        # Asserts if the tags have specific text
        self.assertIn("Välkommen till APIskolan!", masthead_h1.text)
        self.assertIn("En svensk lärplattform för APIer", masthead_h2.text)
