import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class test_DeleteAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # Create a dictionary to store variables if needed
        self.vars = {}

    # This method is called after each test method to clean up resources.
    def teardown_method(self, method):
        # Quit/close the WebDriver to release browser resources
        self.driver.quit()

    # The above class defines a test case for editing an account using the Guru99 website.
    # The `setup_method` method initializes the WebDriver before each test and the
    # `teardown_method` method closes the WebDriver after each test.

    def test_dA1(self):
        # Load the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the "UserID" field, click on it, and input the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the "Password" field, click on it, and input the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Find the "Login" button and click it
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Find the "Delete Account" link and click it
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        # Find the "Account No" field, click on it, and move to the next element
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        # Find elements with the specified ID and check their length
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_dA2(self):
        # Load the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the "UserID" field, click on it, and input the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the "Password" field, click on it, and input the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Find the "Login" button and click it
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Find the "Delete Account" link and click it
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        # Find the "Account No" field, click on it, and input an account number
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1234Acc123")
        # Find elements with the specified ID and check their length
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_dA3(self):
        # Load the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the "UserID" field, click on it, and input the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the "Password" field, click on it, and input the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Find the "Login" button and click it
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Find the "Delete Account" link and click it
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        # Find the "Account No" field, click on it, and input an account number
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#!@#")
        # Find elements with the specified ID and check their length
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_dA4(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_dA5(self):
        # Load the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the "UserID" field, click on it, and input the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the "Password" field, click on it, and input the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Find the "Login" button and click it
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Find the "Delete Account" link and click it
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        # Find the "Account No" field, click on it, input an account number, and press the Tab key
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(" ", Keys.TAB)
        # Find elements with the specified ID and check their length
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_dA6(self):
        # Load the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the "UserID" field, click on it, and input the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the "Password" field, click on it, and input the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Find the "Login" button and click it
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Find the "Delete Account" link and click it
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        # Find the "Account No" field, click on it, and input an account number
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("134249")
        # Find elements with the specified ID and check their length
        elements = self.driver.find_elements(By.ID, "message2")
        # Find the "Submit" button and click it
        self.driver.find_element(By.NAME, "AccSubmit").click()
        assert len(elements) > 0

    def test_dA7(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("12345")
        elements = self.driver.find_elements(By.ID, "message2")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        assert len(elements) > 0

    def test_dA8(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer123456")
        elements = self.driver.find_elements(By.ID, "message2")
        self.driver.find_element(By.NAME, "res").click()
        assert len(elements) > 0


if __name__ == "__main__":
    unittest.main()
