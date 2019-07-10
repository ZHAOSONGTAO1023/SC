import unittest

import time
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()