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


class test_NewAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # A dictionary to hold variables, might be used later.

    def teardown_method(self, method):
        self.driver.quit()  # Close the WebDriver instance after each test.

    def test_NA1(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)  # Pressing the TAB key
        elements = self.driver.find_elements(By.ID, "message14")

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA2(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("1234Acc123")  # Entering customer ID
        elements = self.driver.find_elements(By.ID, "message14")

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA3(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Adding a sleep delay (not the best practice, consider using explicit waits)
        time.sleep(1)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#!@#", Keys.TAB)  # Entering special characters
        elements = self.driver.find_elements(By.ID, "message14")

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA4(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID with space
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12", Keys.TAB)  # Entering a space in customer ID
        elements = self.driver.find_elements(By.ID, "message14")

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA5(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID with space
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(" ", Keys.TAB)  # Entering a space-prefixed customer ID
        elements = self.driver.find_elements(By.ID, "message14")

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA6(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("11258")

        # Move to the initial deposit field and press the TAB key
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys(Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message14")

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA7(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("11258")

        # Input an invalid initial deposit value
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("1234AccAcc123")
        elements = self.driver.find_elements(By.ID, "message14")

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA8(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("11258")

        # Input an invalid initial deposit value
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("123!@#!@#")
        elements = self.driver.find_elements(By.ID, "message14")

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA9(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("11258")

        # Input an invalid initial deposit value with space
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("123 12", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message14")

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA10(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("11258")

        # Input an initial deposit value with spaces and press TAB
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys(" ", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message14")

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA11(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("11258")

        # Select a savings account and input an initial deposit value
        self.driver.find_element(By.NAME, "selaccount").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("Savings")
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("11258", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message14")

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA12(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("11258")

        # Select a current account and input an initial deposit value
        self.driver.find_element(By.NAME, "selaccount").click()
        self.driver.find_element(By.NAME, "selaccount").send_keys("Current")
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("11258", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message14")

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA13(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("qwer")

        # Select a current account and input an initial deposit value
        self.driver.find_element(By.NAME, "selaccount").click()
        self.driver.find_element(By.NAME, "selaccount").send_keys("Current")
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("123456", Keys.TAB)

        # Find elements with ID "message14" and click reset button
        elements = self.driver.find_elements(By.ID, "message14")
        self.driver.find_element(By.NAME, "reset").click()

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA14(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID with leading spaces
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("    123456")

        # Select a savings account and input an initial deposit value
        self.driver.find_element(By.NAME, "selaccount").click()
        self.driver.find_element(By.NAME, "selaccount").send_keys("Savings")
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("12000", Keys.TAB)

        # Find elements with ID "message14" and click the "Submit" button
        elements = self.driver.find_elements(By.ID, "message14")
        self.driver.find_element(By.NAME, "button2").click()

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA15(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("11258")

        # Select a savings account and input an initial deposit value
        self.driver.find_element(By.NAME, "selaccount").click()
        self.driver.find_element(By.NAME, "selaccount").send_keys("Savings")
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("12000", Keys.TAB)

        # Find elements with ID "message14" and click the "Submit" button
        elements = self.driver.find_elements(By.ID, "message14")
        self.driver.find_element(By.NAME, "button2").click()

        # Assertion to check if elements with ID "message14" exist
        assert len(elements) > 0

    def test_NA16(self):
        # Open the website and set window size
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)

        # Fill in login credentials and click login button
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()

        # Navigate to "New Account" and input customer ID
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("11258")

        # Select a savings account and input an initial deposit value
        self.driver.find_element(By.NAME, "selaccount").click()
        self.driver.find_element(By.NAME, "selaccount").send_keys("Savings")
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("12000", Keys.TAB)

        # Find elements with ID "message14" and click the "Submit" button
        elements = self.driver.find_elements(By.ID, "message14")
        self.driver.find_element(By.NAME, "button2").click()

        # Click the "Continue" link and perform an assertion
        self.driver.find_element(By.LINK_TEXT, "Continue").click()
        assert len(elements) > 0


# Check if this script is being run directly (not imported)
if __name__ == "__main__":
    unittest.main()
