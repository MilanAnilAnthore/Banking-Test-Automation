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


class TestMiniStatement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_mS1(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_mS2(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1234Acc123", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_mS3(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@3!@#")
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_mS4(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_mS5(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(" ", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_mS6(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("134249")
        self.driver.find_element(By.NAME, "AccSubmit").click()

    def test_mS7(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("12345")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_mS8(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer123456")
        self.driver.find_element(By.NAME, "res").click()
        account_no_value = self.driver.find_element(By.NAME, "accountno").get_attribute("value")
        self.assertEqual(account_no_value, "")


if __name__ == '__main__':
    unittest.main()
