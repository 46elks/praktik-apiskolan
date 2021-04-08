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

    def test_masthead(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Finds the tags for masthead
        masthead = driver.find_element(By.ID, "indexMasthead")
        masthead_h1 = masthead.find_element(By.TAG_NAME, "h1")
        masthead_h2 = masthead.find_element(By.TAG_NAME, "h2")

        # Asserts if the tags have specific text
        self.assertIn("Välkommen till APIskolan!", masthead_h1.text)
        self.assertIn("En svensk lärplattform för APIer", masthead_h2.text)

    def test_info_links(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        info_section = driver.find_element(By.ID, "info")
        link_elements = info_section.find_elements(By.TAG_NAME, "a")

        # Adds link names to array
        links = []
        for element in link_elements:
            links.append(element.get_attribute("href"))

        # Asserts if links are present in info
        self.assertIn("https://joakim2tusen.github.io/Portfolio/", links)
        self.assertIn("https://klado555.gitlab.io/portfolio/", links)
        self.assertIn("https://github.com/46elks/praktik-apiskolan/", links)

