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

        # Asserts if the wrapper of content page is found
        self.assertIn("contentWrapper", driver.page_source)
    
    def test_image(self):
        driver = self.driver
        driver.get(self.get_url_to("content"))

        # Gets undraw image in content page
        image = driver.find_element(By.ID, "undrawCodeThinking").get_attribute("src")
        self.assertIn("undraw_code_thinking.svg", image)

    def test_quiz_correct_answer(self):
        driver = self.driver
        driver.get(self.get_url_to("content"))
        
        # Gets the correct answer for the quiz
        quiz = driver.find_element(By.ID, "quiz")
        correct_answer = quiz.get_attribute("data-answer")
        
        # Finds and clicks on the correct answer
        quiz_answers = quiz.find_element(By.ID, "quizAnswers")
        correct_quiz_selection = quiz_answers.find_element(By.XPATH, "//input[@value=" + correct_answer + "]")
        correct_quiz_selection.click()

        # Finds and clicks on the submit button
        submit_button = quiz.find_element(By.XPATH, "//input[@type='button']")
        submit_button.click()

        # Switches to alert, asserts if "rätt" is found in it, and then closes the alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        self.assertIn("rätt", alert_text.lower())
        alert.accept()

    def test_quiz_wrong_answer(self):
        driver = self.driver
        driver.get(self.get_url_to("content"))

        # Gets the correct answer for the quiz
        quiz = driver.find_element(By.ID, "quiz")
        correct_answer = quiz.get_attribute("data-answer")

        # Sets a variable containing a different answer than the correct one
        quiz_answers = quiz.find_element(By.ID, "quizAnswers")
        quiz_answer_amount = len(quiz_answers.find_elements(By.XPATH, "//input[@name='quizOption']"))
        wrong_answer = str((int(correct_answer) + 1) % quiz_answer_amount)

        # Gets alert text of the correct answer
        correct_answer_text = quiz_answers.find_element(By.XPATH, "//input[@value=" + correct_answer + "]").find_element(By.XPATH, "..").text

        # Finds and clicks on the incorrect answer
        incorrect_quiz_selection = quiz_answers.find_element(By.XPATH, "//input[@value=" + wrong_answer + "]")
        incorrect_quiz_selection.click()

        # Finds and clicks on the submit button
        submit_button = quiz.find_element(By.XPATH, "//input[@type='button']")
        submit_button.click()

        # Switches to alert, asserts if "fel" is found in it, and then closes the alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        self.assertIn(correct_answer_text, alert_text)
        alert.accept()
