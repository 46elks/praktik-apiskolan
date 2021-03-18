from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestContentPage(WebTestBase):

    def test_navigate_to_page(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)
        
        # Attempts to navigate to content page
        navbar_nav = driver.find_element(By.CLASS_NAME, "navbar-nav")
        content_button = navbar_nav.find_element(By.XPATH, "//a[@href='content.html']")
        content_button.click()

        self.assertIn("contentWrapper", driver.page_source)
    
    def test_image(self):
        driver = self.driver
        driver.get(self.get_url_to("content"))
        
        result = False

        # Attempts to find photo in content page
        photo = driver.find_element(By.TAG_NAME, "img")

        # Checks if image contains "src" attribute
        if photo.get_attribute("src") != None:
            result = True

        self.assertTrue(result)

    def test_quiz_correct(self):
        driver = self.driver
        driver.get(self.get_url_to("content"))
        
        # Looks for the right answer
        quiz = driver.find_element(By.ID, "quiz")
        correct_answer = quiz.get_attribute("data-answer")
        
        # Sets right answer
        answer_try = quiz.find_element(By.TAG_NAME, "input")
        answer_try_click = answer_try.find_element(By.XPATH, "//input[@value=" + correct_answer + "]")
        answer_try_click.click()

        # Clicks check button
        button = quiz.find_element(By.TAG_NAME, "input")
        button_click = button.find_element(By.XPATH, "//input[@value='Svara']")
        button_click.click()

        # Reads alert text and controls it
        alert = driver.switch_to.alert
        alert_text = alert.text
        self.assertIn("rätt", alert_text.lower())
        alert.accept()

    def test_quiz_incorrect(self):
        driver = self.driver
        driver.get(self.get_url_to("content"))

        # Amount of answers
        quiz_answers = driver.find_element(By.ID, "quizAnswers")
        amount_quiz_answers = len(quiz_answers.find_elements(By.XPATH, "//input[@name='quizOption']"))

        # Looks for the right answer
        quiz = driver.find_element(By.ID, "quiz")
        correct_answer = quiz.get_attribute("data-answer")
        wrongAnswer = (int(correct_answer) + 1) % amount_quiz_answers

        # Sets right answer
        answer_try = quiz.find_element(By.TAG_NAME, "input")
        answer_try_click = answer_try.find_element(By.XPATH, "//input[@value=" + str(wrongAnswer) + "]")
        answer_try_click.click()

        # Clicks check button
        button = quiz.find_element(By.TAG_NAME, "input")
        button_click = button.find_element(By.XPATH, "//input[@value='Svara']")
        button_click.click()

        # Reads alert text and controls it
        alert = driver.switch_to.alert
        alert_text = alert.text
        self.assertIn("fel", alert_text.lower())
        alert.accept()

