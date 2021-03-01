#!/usr/bin/env python3
import unittest, os, sys
from subprocess import check_output
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class WebTestBase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.WEBSITE_URL = "file://" + os.getcwd() + "/../../dist/index.html"

        # Checks for valid installations of Firefox.
        try:
            firefox_binary = check_output(['which', 'firefox-esr']).decode().strip()
        except:
            try:
                firefox_binary = check_output(["which", "firefox"]).decode().strip()
            except:
                print("Firefox does not seem to be installed. Please install and use Firefox for running these automated tests!")
                sys.exit(1)

        # Sets up Firefox options and path to geckodriver.
        ops = Options()
        ops.headless = True
        ops.binary_location = firefox_binary

        self.driver = webdriver.Firefox(executable_path=os.getcwd()+"/../geckodriver", options=ops)

        self.driver.implicitly_wait(3)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
