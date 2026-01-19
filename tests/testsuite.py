# Group Project: Test Automation of Banking Project
#
# Group 10
# Durham College
# INFT 1207-04: Software Testing and Automation
# Praveen Raju Gunasekaran 
# 17 April 2024
#
# A program to run the tests for each module of the Banking Project site.

import unittest
from time import sleep

import test_newcustomer
import editcustomer_test
import deletecustomer_test
import test_NewAccount
import test_EditAccount
import test_delete_account
import test_balanceEnquiry
import test_ministatement
import test_custom

# Constants for test suite selection
TEST_NEW_CUSTOMER = 'NC'
TEST_EDIT_CUSTOMER = 'EC'
TEST_DELETE_CUSTOMER = 'DC'
TEST_NEW_ACCOUNT = 'NA'
TEST_EDIT_ACCOUNT = 'EA'
TEST_DELETE_ACCOUNT = 'DA'
TEST_BALANCE_ENQUIRY = 'BE'
TEST_MINI_STATEMENT = 'MS'
TEST_CUSTOMIZED_STATEMENT = 'CS'
SELECT_ALL_TESTS = 'A'
SELECT_QUIT = 'Q'

TEST_CHOICES = {TEST_NEW_CUSTOMER, TEST_EDIT_CUSTOMER, TEST_DELETE_CUSTOMER, TEST_NEW_ACCOUNT, TEST_EDIT_ACCOUNT,
                TEST_DELETE_ACCOUNT, TEST_BALANCE_ENQUIRY, TEST_MINI_STATEMENT, TEST_CUSTOMIZED_STATEMENT,
                SELECT_ALL_TESTS}


def add_suite(test_class, test_suite):
    """Add test module to the test suite"""
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_class))


def run_tests():
    # Set up the testing suite menu.
    choice = ''
    while choice != SELECT_QUIT:
        print(f"""

    Please enter one of the following option:
        - '{TEST_NEW_CUSTOMER}' to test the New Customer module
        - '{TEST_EDIT_CUSTOMER}' to test the Edit Customer module
        - '{TEST_DELETE_CUSTOMER}' to test the Delete Customer module
        - '{TEST_NEW_ACCOUNT}' to test the New Account module
        - '{TEST_EDIT_ACCOUNT}' to test the Edit Account module
        - '{TEST_DELETE_ACCOUNT}' to test the Delete Account module
        - '{TEST_BALANCE_ENQUIRY}' to test the Balance Enquiry module
        - '{TEST_MINI_STATEMENT}' to test the Mini Statement module
        - '{TEST_CUSTOMIZED_STATEMENT}' to test the Customized Statement module
        - '{SELECT_ALL_TESTS}' to run all tests
        
        - '{SELECT_QUIT}' to quit
    """)

        # Create empty test suite
        tests_to_run = unittest.TestSuite()

        # Get the choice from the user.
        choice = input("What would you like to do? ").upper()
        if choice in (TEST_NEW_CUSTOMER, SELECT_ALL_TESTS):
            add_suite(test_newcustomer.TestTestsuiteNC, tests_to_run)

        elif choice in (TEST_EDIT_CUSTOMER, SELECT_ALL_TESTS):
            add_suite(editcustomer_test.Test2, tests_to_run)

        elif choice in (TEST_DELETE_CUSTOMER, SELECT_ALL_TESTS):
            add_suite(deletecustomer_test.Test3, tests_to_run)

        elif choice in (TEST_NEW_ACCOUNT, SELECT_ALL_TESTS):
            add_suite(test_NewAccount.test_NewAccount, tests_to_run)

        elif choice in (TEST_EDIT_ACCOUNT, SELECT_ALL_TESTS):
            add_suite(test_EditAccount.test_EditAccount, tests_to_run)

        elif choice in (TEST_DELETE_ACCOUNT, SELECT_ALL_TESTS):
            add_suite(test_delete_account, tests_to_run)
            print('This test suite is not finished yet.')

        elif choice in (TEST_BALANCE_ENQUIRY, SELECT_ALL_TESTS):
            add_suite(test_balanceEnquiry.TestBalanceEnquiry, tests_to_run)

        elif choice in (TEST_MINI_STATEMENT, SELECT_ALL_TESTS):
            add_suite(test_ministatement.TestMiniStatement, tests_to_run)

        elif choice in (TEST_CUSTOMIZED_STATEMENT, SELECT_ALL_TESTS):
            add_suite(test_custom.TestCustomStatement, tests_to_run)

        # Run the tests.
        if choice in TEST_CHOICES:
            # Run the selected tests.
            runner = unittest.TextTestRunner()
            runner.run(tests_to_run)

            # Wait for the tests to finish running.
            sleep(3)


if __name__ == '__main__':
    run_tests()
