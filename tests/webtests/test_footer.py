from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestFooter(WebTestBase):

    def test_links(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Gets footer element on page
        footer = driver.find_element(By.TAG_NAME, "footer")

        # Gets all links in footer
        link_elements = footer.find_elements(By.TAG_NAME, "a")

        # Adds link names to array
        links = []
        for element in link_elements:
            links.append(element.get_attribute("href"))

        # Asserts if links are present in footer
        self.assertIn("https://github.com/46elks/", links)
        self.assertIn("https://medium.com/46elks/", links)
        self.assertIn("https://twitter.com/46elks/", links)
        self.assertIn("https://www.instagram.com/46elks/", links)
        self.assertIn("https://www.facebook.com/46elks/", links)
        self.assertIn("https://46elks.se/", links)

