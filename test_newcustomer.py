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


class TestTestsuiteNC(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_NC1(self):
        # login
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        time.sleep(1)
        # entering username  and password
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        # clicking on new customer and entering customer details
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        # enter tab keys to the customer name field
        self.driver.find_element(By.NAME, "name").send_keys(Keys.TAB)
        time.sleep(1)
        # finding elements with the ID "message"
        elements = self.driver.find_elements(By.ID, "message")
        time.sleep(2)
        assert len(elements) > 0

    def test_NC2(self):
        # login and entering username and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        # input numbers to the customer name field
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("1234")
        elements = self.driver.find_elements(By.ID, "message")
        assert len(elements) > 0

    def test_NC3(self):
        # login and entering username and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(974, 1050)
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        # inputting special characters in the customer name field
        self.driver.find_element(By.NAME, "name").send_keys("name!@#")
        time.sleep(1)
        elements = self.driver.find_elements(By.ID, "message")
        assert len(elements) > 0

    def test_NC4(self):
        # login and entering username and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        # inputting space  in the customer name field
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys(" ")
        elements = self.driver.find_elements(By.ID, "message")
        time.sleep(2)
        assert len(elements) > 0

    def test_NC5(self):
        # login and entering username and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        # entering tab keys to the address field
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message3")
        time.sleep(2)
        assert len(elements) > 0

    def test_NC6(self):
        # login and entering username and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        # entering space in the address field
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys(" ")
        time.sleep(1)
        elements = self.driver.find_elements(By.ID, "message3")
        time.sleep(2)
        assert len(elements) > 0

    def test_NC7(self):
        # login and entering username and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        # entering tab keys to the city field
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        time.sleep(1)
        elements = self.driver.find_elements(By.ID, "message4")
        assert len(elements) > 0

    def test_NC8(self):
        # login to the site and enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        # select new customer
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "city").click()
        time.sleep(1)
        # adding  numbers to the city field
        self.driver.find_element(By.NAME, "city").send_keys("1234city123")
        time.sleep(1)
        elements = self.driver.find_elements(By.ID, "message4")
        assert len(elements) > 0

    def test_NC9(self):
        # login to the site and enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        # select new customer
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        # entering special characters in the city field
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("city!@^!#")
        time.sleep(1)
        elements = self.driver.find_elements(By.ID, "message4")
        assert len(elements) > 0

    def test_NC10(self):
        # login to the site and enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        # select new customer
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        # enter space in the city field
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("  ")
        time.sleep(1)
        elements = self.driver.find_elements(By.ID, "message4")
        assert len(elements) > 0

    def test_NC11(self):
        # login to the site and enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        # entering tab keys to the state field
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        time.sleep(1)
        elements = self.driver.find_elements(By.ID, "message5")
        assert len(elements) > 0

    def test_NC12(self):
        # login to the site and enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "state").click()
        # entering numbers to the state field
        time.sleep(1)
        self.driver.find_element(By.NAME, "state").send_keys("124 state 123")
        time.sleep(1)
        elements = self.driver.find_elements(By.ID, "message5")
        assert len(elements) > 0

    def test_NC13(self):
        # login to the site and enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        # adding special characters to the state field
        self.driver.find_element(By.NAME, "state").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "state").send_keys("state@#$!")
        time.sleep(1)
        elements = self.driver.find_elements(By.ID, "message5")
        assert len(elements) > 0

    def test_NC14(self):
        # login to the site and enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        # entering space in the state field
        self.driver.find_element(By.NAME, "state").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "state").send_keys(" ")
        elements = self.driver.find_elements(By.ID, "message5")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC15(self):
        # login to the site and enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        # entering tab keys to the pinno field
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234PIN")
        elements = self.driver.find_elements(By.ID, "message6")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC16(self):
        # login to the site and enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        # enter tab key to the pinno field
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message6")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC17(self):
        # enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        time.sleep(1)
        # adding less numb to the pinno field
        self.driver.find_element(By.NAME, "pinno").send_keys("12")
        elements = self.driver.find_elements(By.ID, "message6")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC18(self):
        # enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        # enter special characters to the pinno field
        time.sleep(1)
        self.driver.find_element(By.NAME, "pinno").send_keys("!@#123!")
        elements = self.driver.find_elements(By.ID, "message6")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC19(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "pinno").click()
        # entering space in the p field
        self.driver.find_element(By.NAME, "pinno").send_keys(" ")
        elements = self.driver.find_elements(By.ID, "message6")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC20(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "pinno").click()
        # entering
        time.sleep(1)
        self.driver.find_element(By.NAME, "pinno").send_keys(" ")
        elements = self.driver.find_elements(By.ID, "message6")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC21(self):
        # login to the site and enter manager id and password
        time.sleep(1)
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        # adding tab key to the telephoneno field
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message7")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC22(self):
        # login to the site and enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys(" ")
        elements = self.driver.find_elements(By.ID, "message7")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC23(self):
        # login to the site and enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        # entering characters to the telephoneno field
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("123 123")
        elements = self.driver.find_elements(By.ID, "message7")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC24(self):
        # login to the site and enter manager id and password
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        time.sleep(1)
        # entering special characters to the telephoneno field
        self.driver.find_element(By.NAME, "telephoneno").send_keys("886636!@12")
        elements = self.driver.find_elements(By.ID, "message7")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC25(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message9")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC26(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        time.sleep(1)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail")
        elements = self.driver.find_elements(By.ID, "message9")
        time.sleep(1)
        assert len(elements) > 0

    def test_NC27(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "emailid").send_keys(" ")
        self.driver.find_element(By.NAME, "emailid").click()

    def test_NC28(self):
        self.driver.get("https://demo.guru99.com/v4/")
        self.driver.set_window_size(945, 1030)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr567239")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("gAtEsem")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "emailid").click()
        time.sleep(1)
        # entering tab key to the emailid field
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        elements = self.driver.find_elements(By.ID, "message18")
        assert len(elements) > 0


def run_tests():
    unittest.main()
