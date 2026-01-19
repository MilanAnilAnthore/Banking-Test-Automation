import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Test3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "https://demo.guru99.com/V4/"

    def test_DC1(self):
        driver = self.driver
        driver.get(self.base_url)

        # Step 1: Fill in username and password and click login
        user_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()

        delete_customer = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Delete Customer")))
        delete_customer.click()

        # Step 1: Click the Submit button without entering any value in the Customer id field
        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Please fill all fields")
        alert.dismiss()  # Dismiss the alert    

    def test_DC2(self):
        driver = self.driver
        driver.get(self.base_url)

        # Step 1: Fill in username and password and click login
        user_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()

        delete_customer = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Delete Customer")))
        delete_customer.click()
        # Step 2: Enter a character value in the Customer id field and click Submit
        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("Acc123")

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message14"))).text
        self.assertEqual(error_message, "Characters are not allowed")
        cust_id.clear()

    def test_DC3(self):
        driver = self.driver
        driver.get(self.base_url)

        # Step 1: Fill in username and password and click login
        user_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()

        delete_customer = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Delete Customer")))
        delete_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("123!@#!@#")

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message14"))).text
        self.assertEqual(error_message, "Special characters are not allowed")
        cust_id.clear()

    def test_DC4(self):
        driver = self.driver
        driver.get(self.base_url)

        # Step 1: Fill in username and password and click login
        user_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()

        delete_customer = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Delete Customer")))
        delete_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("123 12")

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message14"))).text
        self.assertEqual(error_message, "Characters are not allowed")
        cust_id.clear()
        cust_id.send_keys(Keys.TAB)

    def test_DC5(self):
        driver = self.driver
        driver.get(self.base_url)

        # Step 1: Fill in username and password and click login
        user_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()

        delete_customer = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Delete Customer")))
        delete_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys(" ")

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "message14"))).text
        self.assertEqual(error_message, "First character can not have space")
        cust_id.clear()
        cust_id.send_keys(Keys.TAB)

    def test_DC6(self):
        driver = self.driver
        driver.get(self.base_url)

        # Step 1: Fill in username and password and click login
        user_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()

        delete_customer = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Delete Customer")))
        delete_customer.click()

        # Step 2: Enter a valid customer ID and click Submit
        cust_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("123456")

        submit = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()

        # Verify the confirmation alert for deletion
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Do you really want to delete this Customer?")
        alert.accept()

        # Verify the alert indicating that the customer doesn't exist
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Customer does not exist!!")
        alert.accept()

        # Clear the customer ID field for the next test case
        cust_id.clear()
        cust_id.send_keys(Keys.TAB)

    def test_DC7(self):
        driver = self.driver
        driver.get(self.base_url)

        # Step 1: Fill in username and password and click login
        user_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()

        delete_customer = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Delete Customer")))
        delete_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("11258")
        submit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "AccSubmit")))
        submit.click()
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Do you really want to delete this Customer?")
        alert.dismiss()
        cust_id.send_keys(Keys.TAB)

    def test_DC8(self):
        driver = self.driver
        driver.get(self.base_url)

        # Step 1: Fill in username and password and click login
        user_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid")))
        user_id.send_keys("mngr567239")

        password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("gAtEsem")

        login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login.click()

        delete_customer = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Delete Customer")))
        delete_customer.click()

        cust_id = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))
        cust_id.send_keys("qwer")
        reset = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "res")))
        reset.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
