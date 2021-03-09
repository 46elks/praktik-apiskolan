from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestContentPage(WebTestBase):
    
    def test_title(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Attempts navigate to content page
        navbar = driver.find_element(By.ID, "mainNav")
        navbar_nav = navbar.find_element(By.CLASS_NAME, "navbar-nav")
        navbar_names = navbar_nav.find_element(By.XPATH, "//a[@href='content.html']")
        navbar_names.click()

        # Attempts to find title in content page
        navbar_title = driver.find_element(By.TAG_NAME, "h1")
        assert navbar_title.text == "Vad är ett API?"

    def test_image(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        
        # Attempts navigate to content page
        navbar = driver.find_element(By.ID, "mainNav")
        navbar_nav = navbar.find_element(By.CLASS_NAME, "navbar-nav")
        navbar_names = navbar_nav.find_element(By.XPATH, "//a[@href='content.html']")
        navbar_names.click()
        
        result = False

        # Attempts to find photo in content page
        photo = driver.find_element(By.TAG_NAME, "img")

        # Checks if logo contains "src" attribute
        if photo.get_attribute("src") != None:
            result = True

        self.assertTrue(result)
