> ⚠️ Academic Project Notice  
> This repository represents a completed academic project (April 2024) and is preserved for learning, reference, and portfolio purposes.


# Banking Test Automation (Guru99 Demo Bank)

Automated UI test suite for the [Guru99 demo banking site](https://demo.guru99.com/v4/) created as part of Durham College INFT 1207 (Software Testing and Automation), Group 10, April 2024. The suite uses Python’s `unittest` framework with Selenium WebDriver to validate key banking workflows and input validation messages across multiple modules.

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Repository Structure](#repository-structure)
- [Test Modules Covered](#test-modules-covered)
- [Installation and Setup](#installation-and-setup)
- [Running the Tests](#running-the-tests)
- [Test Reports](#test-reports)
- [Credentials and Test Data](#credentials-and-test-data)
- [Known Limitations and Future Improvements](#known-limitations-and-future-improvements)
- [Project Report](#project-report)
- [Acknowledgements](#acknowledgements)


---

## Overview

This project automates end-to-end validation scenarios on the Guru99 demo banking site, focusing on:
- UI navigation and form submissions
- Error and validation messaging
- Functional flows for customer and account operations

It includes both interactive suite execution and individual test execution support. The design centers around straightforward `unittest` test cases with Selenium Chrome WebDriver.

## Tech Stack

- Language: Python
- Framework: `unittest`
- UI Automation: Selenium WebDriver (Chrome)
- Reports: HTML reports generated and stored in `test-reports html/`
- Target App: Guru99 Demo Bank UI

## Repository Structure

Key files and directories:
- Root-level test modules:
  - [testsuite.py](https://github.com/MilanAnilAnthore/Banking-Test-Automation/blob/main/testsuite.py): Interactive test runner with menu for selecting module suites (New Customer, Edit Customer, Delete Customer, New Account, Edit Account, Delete Account, Balance Enquiry, Mini Statement, Customized Statement).
  - [test_newcustomer.py](https://github.com/MilanAnilAnthore/Banking-Test-Automation/blob/main/test_newcustomer.py)
  - [editcustomer_test.py](https://github.com/MilanAnilAnthore/Banking-Test-Automation/blob/main/editcustomer_test.py)
  - [deletecustomer_test.py](https://github.com/MilanAnilAnthore/Banking-Test-Automation/blob/main/deletecustomer_test.py)
  - [test_NewAccount.py](https://github.com/MilanAnilAnthore/Banking-Test-Automation/blob/main/test_NewAccount.py)
  - [test_EditAccount.py](https://github.com/MilanAnilAnthore/Banking-Test-Automation/blob/main/test_EditAccount.py)
  - [test_Deleteaccount.py](https://github.com/MilanAnilAnthore/Banking-Test-Automation/blob/main/test_Deleteaccount.py)
  - [test_balanceEnquiry.py](https://github.com/MilanAnilAnthore/Banking-Test-Automation/blob/main/test_balanceEnquiry.py)
  - [test_ministatement.py](https://github.com/MilanAnilAnthore/Banking-Test-Automation/blob/main/test_ministatement.py)
  - [test_custom.py](https://github.com/MilanAnilAnthore/Banking-Test-Automation/blob/main/test_custom.py)

- Reports:
  - `test-reports html/` folder containing HTML test result pages such as:
    - Test_Results_Newcustomer.html
    - Test_Results_Editcustomer.html
    - Test_Results_Deletecustomer.html
    - Test_Results_Newaccount.html
    - Test_Results_Editaccount.html
    - Test_Results_Deleteaccount.html
    - Test_Results_Balanceenquiry.html
    - Test_Results_Ministatement.html
    - “TestSutieCases - .html”

- Documentation:
  - “INFT 1207- Project Report GROUP 10.pdf” (Project report with test documentation and context)

Note: In some branches/commits, tests also appear within a `tests/` directory reflecting expanded suites (e.g., `tests/test_NewAccount.py`, `tests/test_balanceEnquiry.py`). Use discovery commands accordingly.

## Test Modules Covered

Each module logs in to the demo bank and navigates to the relevant page:
- New Customer: `test_newcustomer.py`
  - Validates customer name input (empty, numeric, special chars) and checks validation message (`id="message"`).
- Edit Customer: `editcustomer_test.py`
  - Validates customer ID entry and error handling, including alerts (“Please fill all fields”, “Customer ID is required”, “Characters are not allowed”).
- Delete Customer: `deletecustomer_test.py`
  - Validates alert behavior and ID validation (“Characters are not allowed”) on delete customer flow.
- New Account: `test_NewAccount.py`
  - Validates customer ID input, account type selection, initial deposit, and checks for validation messages (`id="message14"`).
- Edit Account: `test_EditAccount.py`
  - Validates account number input and checks validation messages (`id="message2"`).
- Delete Account: `test_Deleteaccount.py`
  - Validates account number input and checks validation messages (`id="message2"`). Note: In the interactive suite, delete account is marked “not finished yet.”
- Balance Enquiry: `test_balanceEnquiry.py`
  - Validates account number input including tabs, alphanumeric, special chars; checks validation messages (`id="message2"`) and submission behavior.
- Mini Statement: `test_ministatement.py`
  - Similar validations for account number and message handling (`id="message2"`).
- Customized Statement: `test_custom.py`
  - Validates account number formats and the presence of validation messages (`id="message2"`); includes scenarios to reset and verify fields are cleared.

## Installation and Setup

1. Prerequisites:
   - Python 3.10+ (recommended)
   - Google Chrome installed
   - ChromeDriver available in your PATH and matching your Chrome version
     - Download: https://chromedriver.chromium.org/downloads

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install selenium
   ```
   Optional convenience:
   ```bash
   pip install webdriver-manager
   ```
   If you use `webdriver-manager`, you can modify driver creation in tests from:
   ```python
   self.driver = webdriver.Chrome()
   ```
   to:
   ```python
   from webdriver_manager.chrome import ChromeDriverManager
   from selenium.webdriver.chrome.service import Service
   self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   ```

## Running the Tests

You can run the interactive suite menu or individual modules.

### Option A: Interactive Test Suite Menu
Runs a menu that lets you select specific module suites:
```bash
python testsuite.py
```
Menu options in `testsuite.py`:
- NC: New Customer
- EC: Edit Customer
- DC: Delete Customer
- NA: New Account
- EA: Edit Account
- DA: Delete Account (prints “not finished yet” in the suite)
- BE: Balance Enquiry
- MS: Mini Statement
- CS: Customized Statement
- A: Run all tests
- Q: Quit

### Option B: Run a Single Test File
Use Python’s unittest runner directly:
```bash
python -m unittest test_newcustomer.TestTestsuiteNC
python -m unittest editcustomer_test.Test2
python -m unittest deletecustomer_test.Test3
python -m unittest test_NewAccount.test_NewAccount
python -m unittest test_EditAccount.test_EditAccount
python -m unittest test_Deleteaccount.test_DeleteAccount
python -m unittest test_balanceEnquiry.TestBalanceEnquiry
python -m unittest test_ministatement.TestMiniStatement
python -m unittest test_custom.TestCustomStatement
```

### Option C: Discover and Run All Tests Automatically
If tests are in the repository root:
```bash
python -m unittest discover -p "test_*.py"
```
If tests are in a `tests/` folder:
```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Test Reports

HTML test result pages are stored in:
- `test-reports html/`

Open any of these in a browser to view formatted results, for example:
- Test_Results_Newcustomer.html
- Test_Results_Editcustomer.html
- Test_Results_Deletecustomer.html
- Test_Results_Newaccount.html
- Test_Results_Editaccount.html
- Test_Results_Deleteaccount.html
- Test_Results_Balanceenquiry.html
- Test_Results_Ministatement.html

## Credentials and Test Data

The demo bank credentials used across tests:
- User ID: `mngr567239`
- Password: `gAtEsem`

These are test credentials provided by the Guru99 demo site. Do not use real or sensitive credentials.

## Known Limitations and Future Improvements

- Delete Account suite (DA) is flagged as “not finished yet” in the interactive runner.
- Some tests use `time.sleep`; consider migrating to explicit waits (`WebDriverWait`) for stability.
- ChromeDriver management can be simplified using `webdriver-manager`.
- Add a `requirements.txt` for dependency pinning and reproducible setup.
- Implement a unified test report generation workflow (e.g., `pytest` + `pytest-html`, or `unittest-xml-reporting`).
- Consider page object patterns to reduce duplication and improve maintainability.

## Project Report

A project report PDF is included in the repository:
- “INFT 1207- Project Report GROUP 10.pdf”
This report documents the testing objectives, test design, and results context for the course project.

## Acknowledgements

- Durham College, INFT 1207-04: Software Testing and Automation, Group 10
- Guru99 Demo Bank (https://demo.guru99.com/v4/) for providing a publicly accessible UI for practice and educational automation