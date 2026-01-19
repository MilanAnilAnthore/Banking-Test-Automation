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


class test_EditAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        # Quit the WebDriver instance when the test method finishes
        self.driver.quit()

    def test_eA1(self):
        # Navigate to the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the 'User ID' field, click on it, and enter the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the 'Password' field, click on it, and enter the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Click on the 'Login' button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Click on the 'Edit Account' link
        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()
        # Find the 'Account No' field, click on it, and press the 'Tab' key
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        # Find elements with the specified ID and check if there are elements
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0  # Ensure the length of elements is greater than 0

    def test_eA2(self):
        # Navigate to the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the 'User ID' field, click on it, and enter the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the 'Password' field, click on it, and enter the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Click on the 'Login' button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Click on the 'Edit Account' link
        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()
        # Find the 'Account No' field, click on it, and enter an account number
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1234Acc123")
        # Find elements with the specified ID and check if there are elements
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0  # Ensure the length of elements is greater than 0

    def test_eA3(self):
        # Navigate to the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the 'User ID' field, click on it, and enter the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the 'Password' field, click on it, and enter the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Click on the 'Login' button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Click on the 'Edit Account' link
        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()
        # Find the 'Account No' field, click on it, and enter an invalid account number
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#!@#")
        # Find elements with the specified ID and check if there are elements
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0  # Ensure the length of elements is greater than 0

    def test_eA4(self):
        # Navigate to the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the 'User ID' field, click on it, and enter the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the 'Password' field, click on it, and enter the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Click on the 'Login' button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Click on the 'Edit Account' link
        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()
        # Find the 'Account No' field, click on it, and enter an account number with spaces
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12", Keys.TAB)
        # Find elements with the specified ID and check if there are elements
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0  # Ensure the length of elements is greater than 0

    def test_eA5(self):
        # Navigate to the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the 'User ID' field, click on it, and enter the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the 'Password' field, click on it, and enter the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Click on the 'Login' button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Click on the 'Edit Account' link
        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()
        # Find the 'Account No' field, click on it, and enter an account number with spaces
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(" ", Keys.TAB)
        # Find elements with the specified ID and check if there are elements
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0  # Ensure the length of elements is greater than 0

    def test_eA6(self):
        # Navigate to the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the 'User ID' field, click on it, and enter the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the 'Password' field, click on it, and enter the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Click on the 'Login' button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Click on the 'Edit Account' link
        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()
        # Find the 'Account No' field, click on it, and enter an account number
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("134249")
        # Find elements with the specified ID and check if there are elements
        elements = self.driver.find_elements(By.ID, "message2")
        # Click on the 'Submit' button
        self.driver.find_element(By.NAME, "AccSubmit").click()
        assert len(elements) > 0  # Ensure the length of elements is greater than 0

    def test_eA7(self):
        # Navigate to the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the 'User ID' field, click on it, and enter the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the 'Password' field, click on it, and enter the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Click on the 'Login' button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Click on the 'Edit Account' link
        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()
        # Find the 'Account No' field, click on it, and enter an account number
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("12345", Keys.TAB)
        # Find elements with the specified ID and check if there are elements
        elements = self.driver.find_elements(By.ID, "message2")
        # Click on the 'Submit' button
        self.driver.find_element(By.NAME, "AccSubmit").click()
        # Assert that there are elements present
        assert len(elements) > 0

    def test_eA8(self):
        # Navigate to the Guru99 website
        self.driver.get("https://demo.guru99.com/v4/")
        # Set the window size of the browser
        self.driver.set_window_size(974, 1050)
        # Find the 'User ID' field, click on it, and enter the user ID
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Find the 'Password' field, click on it, and enter the password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Click on the 'Login' button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Click on the 'Edit Account' link
        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()
        # Find the 'Account No' field, click on it, and enter an invalid account number
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer12345")
        # Click on the 'Reset' button
        self.driver.find_element(By.NAME, "res").click()
        # Find elements with the specified ID and check if there are elements
        elements = self.driver.find_elements(By.ID, "message2")
        # Assert that there are elements present
        assert len(elements) > 0


# Execute the test case when the script is run directly
if __name__ == "__main__":
    unittest.main()
