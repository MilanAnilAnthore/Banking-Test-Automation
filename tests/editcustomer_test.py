import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class Test2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "https://demo.guru99.com/V4/"

    def test_EC1(self):
        driver = self.driver
        driver.get(self.base_url)

        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()

        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        # Step 1: Click the Submit button without entering any value in the Customer id field
        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys(Keys.ENTER)
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Please fill all fields")
        alert.dismiss()  # Dismiss the alert

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message14"))).text
        self.assertEqual(error_message, "Customer ID is required")
        cust_id.clear()
        cust_id.send_keys(Keys.TAB)

    def test_EC2(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        # Step 2: Enter a character value in the Customer id field and click Submit
        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("1234Acc")

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message14"))).text
        self.assertEqual(error_message, "Characters are not allowed")
        cust_id.clear()

    def test_EC3(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()
        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("123!@#!@#")

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message14"))).text
        self.assertEqual(error_message, "Special characters are not allowed")
        cust_id.clear()

    def test_EC4(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()
        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()

    def test_EC5(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()
        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")
        # Find elements with ID "message14" and click the "Submit" button
        elements = self.driver.find_elements(By.ID, "message14")
        self.driver.find_element(By.NAME, "button2").click()

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()

        # Step 3: Leave the Address field empty and click Submit
        address = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "addr")))
        address.clear()
        address.send_keys(Keys.TAB)  # Move to the next field

    def test_EC6(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()

        # Step 4: Leave the City field empty and click Submit
        city = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "city")))
        city.clear()
        city.send_keys(Keys.TAB)  # Move to the next field
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message4"))).text
        self.assertEqual(error_message, "City Field must not be blank")

    def test_EC7(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 5: Enter a valid value in the City field and click Submit
        city = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "city")))
        city.send_keys("1234")

        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message4"))).text
        self.assertEqual(error_message, "Numbers are not allowed")
        city.clear()

    def test_EC8(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 6: Enter an invalid value in the City field and click Submit
        city = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "city")))
        city.send_keys("City!@#")

        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message4"))).text
        self.assertEqual(error_message, "Special characters are not allowed")

        # Clear the city field for the next test case
        city.clear()

    def test_EC9(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 7: Leave the State field empty
        state = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "state")))
        state.clear()
        state.send_keys(Keys.TAB)
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message5"))).text
        self.assertEqual(error_message, "State must not be blank")

    def test_EC10(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 8: Enter a valid value in the State field and click Submit
        state = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "state")))
        state.clear()
        state.send_keys("1234")

        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message5"))).text
        self.assertEqual(error_message, "Numbers are not allowed")
        state.clear()

    def test_EC11(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 9: Enter an invalid value in the State field and click Submit
        state = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "state")))
        state.send_keys("State!@#")

        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message5"))).text
        self.assertEqual(error_message, "Special characters are not allowed")

        # Clear the state field for the next test case
        state.clear()

    def test_EC12(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 10: Enter a valid value in the PIN field and click Submit
        pin = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "pinno")))
        pin.send_keys("1234")
        pin.send_keys(Keys.TAB)

    def test_EC13(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 11: Leave the PIN field empty and click Submit
        pin = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "pinno")))
        pin.clear()
        pin.send_keys(Keys.TAB)  # Move to the next field
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message6"))).text
        self.assertEqual(error_message, "PIN Code must not be blank")

    def test_EC14(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 12: Enter more than 6 digits in the PIN field and click Submit
        pin = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "pinno")))
        pin.clear()
        pin.send_keys("1234567")

        # Verify the error message "PIN Code must have 6 Digits"
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message6"))).text
        self.assertEqual(error_message, "PIN Code must have 6 Digits")

    def test_EC15(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 13: Enter special characters in the PIN field and click Submit
        pin = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "pinno")))
        pin.clear()
        pin.send_keys("!@#")

        # Verify the error message "Special characters are not allowed"
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message6"))).text
        self.assertEqual(error_message, "Special characters are not allowed")

    def test_EC16(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 14: Leave the Mobile Number field empty and click Submit
        mobile = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "telephoneno")))
        mobile.clear()

        # Verify the error message "Mobile no must not be blank"
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message7"))).text
        self.assertEqual(error_message, "Mobile no must not be blank")

    def test_EC17(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 17: Enter Special Character In Mobile Number Field and click Submit
        mobile = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "telephoneno")))
        mobile.clear()
        mobile.send_keys("886636!@12")

        # Verify the error message "Special characters are not allowed"
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message7"))).text
        self.assertEqual(error_message, "Special characters are not allowed")

    def test_EC18(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 18: Leave the Email field empty and click Submit
        email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "emailid")))
        email.clear()

        # Verify the error message "Email-ID must not be blank"
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message9"))).text
        self.assertEqual(error_message, "Email-ID must not be blank")

    def test_EC19(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        # Step 19: Enter an invalid email in the Email field and click Submit
        email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "emailid")))
        email.clear()
        email.send_keys("guru99@gmail")

        # Verify the error message "Email-ID is not valid"
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message9"))).text
        self.assertEqual(error_message, "Email-ID is not valid")

    def test_EC20(self):
        driver = self.driver
        driver.get(self.base_url)
        user_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()
        edit_customer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit Customer")))
        edit_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")

        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "emailid")))
        email.clear()
        email.send_keys(" ")
        # Step 20: Click the Submit button after every update
        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "sub")))
        submit.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
