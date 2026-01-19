import unittest
import time
import json

import elements
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestBalanceEnquiry(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_BE1(self):
        # Navigating to the website
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        time.sleep(1)
        # Entering username
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Entering password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Clicking the Login button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Clicking on "Balance Enquiry"
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        time.sleep(1)
        # Clicking on the "accountno" field and then add tab key
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        time.sleep(1)
        # Finding elements with the ID "message2"
        elements = self.driver.find_elements(By.ID, "message2")
        time.sleep(2)
        assert len(elements) > 0

    def test_BE2(self):
        # Navigating to the website
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        time.sleep(1)
        # Entering username
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Entering password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Clicking the Login button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Clicking on "Balance Enquiry"
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        time.sleep(1)
        # Clicking on the "accountno" field and then add numbers and alpabet
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1234 Acc123")
        time.sleep(1)
        # Finding elements with the ID "message2"
        elements = self.driver.find_elements(By.ID, "message2")
        time.sleep(2)
        assert len(elements) > 0

    def test_BE3(self):
        # Navigating to the website
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        time.sleep(1)
        # Entering username
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Entering password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Clicking the Login button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Clicking on "Balance Enquiry"
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        time.sleep(1)
        # Clicking on the "accountno" field and then add special character
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123@^$")
        time.sleep(1)
        # Finding elements with the ID "message2"
        elements = self.driver.find_elements(By.ID, "message2")
        time.sleep(2)
        assert len(elements) > 0

    def test_BE4(self):
        # Navigating to the website
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        time.sleep(1)
        # Entering username
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Entering password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Clicking the Login button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Clicking on "Balance Enquiry"
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        time.sleep(1)
        # Clicking on the "accountno" field and then add space in the field
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(" ", Keys.TAB)
        time.sleep(1)
        # Finding elements with the ID "message2"
        elements = self.driver.find_elements(By.ID, "message2")
        time.sleep(2)
        assert len(elements) > 0

    def test_BE5(self):
        # Navigating to the website
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        time.sleep(1)
        # Entering username
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Entering password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Clicking the Login button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Clicking on "Balance Enquiry"
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        time.sleep(1)
        # Clicking on the "accountno" field and then add space in the field
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("134249")
        time.sleep(1)
        # Finding elements with the ID "message2"
        elements = self.driver.find_elements(By.ID, "message2")
        time.sleep(2)
        assert len(elements) > 0

    def test_BE6(self):
        # Navigating to the website
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        time.sleep(1)
        # Entering username
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Entering password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Clicking the Login button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Clicking on "Balance Enquiry"
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        time.sleep(1)
        # Clicking on the "accountno" field  enter invalid number
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("12345")
        time.sleep(1)
        # submit
        self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()
        time.sleep(1)
        assert len(elements) > 0

    def test_BE7(self):
        # Navigating to the website
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        time.sleep(1)
        # Entering username
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        # Entering password
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        # Clicking the Login button
        self.driver.find_element(By.NAME, "btnLogin").click()
        # Clicking on "Balance Enquiry"
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        time.sleep(1)
        # Clicking on the "accountno" field  enter invalid number
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer   123456")
        time.sleep(1)
        # submit
        self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[2]").click()
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
