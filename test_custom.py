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


class TestCustomStatement(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_cS1(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_cS2(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123Acc123")
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_cS3(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#123")
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_cS4(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_cS5(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(" ", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message2")
        assert len(elements) > 0

    def test_cS6(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(2)").click()
        elements = self.driver.find_elements(By.ID, "message26")
        assert len(elements) > 0

    def test_cS7(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "tdate").click()
        elements = self.driver.find_elements(By.ID, "message27")
        assert len(elements) > 0

    def test_cS8(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("1234Acc123")
        elements = self.driver.find_elements(By.ID, "message12")
        assert len(elements) > 0

    def test_cS9(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("123!@#!@#")
        elements = self.driver.find_elements(By.ID, "message12")
        assert len(elements) > 0

    def test_cS10(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("123 12", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message12")
        assert len(elements) > 0

    def test_cS11(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys(" ", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message12")
        assert len(elements) > 0

    def test_cS12(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("1234Acc123")
        elements = self.driver.find_elements(By.ID, "message13")
        assert len(elements) > 0

    def test_cS13(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("123!@#!@#")
        elements = self.driver.find_elements(By.ID, "message13")
        assert len(elements) > 0

    def test_cS14(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("123 12", Keys.TAB)
        self.driver.find_element(By.NAME, "numtransaction").click()
        elements = self.driver.find_elements(By.ID, "message13")
        assert len(elements) > 0

    def test_cS15(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys(" ", Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message13")
        assert len(elements) > 0

    def test_cS16(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # Enter values in all fields
        self.driver.find_element(By.NAME, "accountno").send_keys("134249")
        self.driver.find_element(By.NAME, "fdate").send_keys("01/01/2024")
        self.driver.find_element(By.NAME, "tdate").send_keys("01/31/2024")
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").send_keys("5")
        # Click Reset Button
        self.driver.find_element(By.NAME, "res").click()
        # Verify all fields are reset
        self.assertEqual(self.driver.find_element(By.NAME, "accountno").get_attribute("value"), "")
        self.assertEqual(self.driver.find_element(By.NAME, "fdate").get_attribute("value"), "")
        self.assertEqual(self.driver.find_element(By.NAME, "tdate").get_attribute("value"), "")
        self.assertEqual(self.driver.find_element(By.NAME, "amountlowerlimit").get_attribute("value"), "")
        self.assertEqual(self.driver.find_element(By.NAME, "numtransaction").get_attribute("value"), "")

    def test_cS17(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        # Enter valid data for Account Number, From Date, Minimum Transaction Value, and Number of Transaction
        self.driver.find_element(By.NAME, "accountno").send_keys("134249")
        self.driver.find_element(By.NAME, "fdate").send_keys("01/01/2024")
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").send_keys("5")
        # Leave To Date field blank
        # Click Submit Button
        self.driver.find_element(By.NAME, "AccSubmit").click()
        # Verify the error message
        error_message = self.driver.find_element(By.ID, "message2").text
        self.assertEqual(error_message, "Please fill all fields")


if __name__ == '__main__':
    unittest.main()
