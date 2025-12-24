"""
- This file contains setup method that created a common webdriver object and returns it.
- This object can be used by other testcases class, by calling the setup() method
- We have the option to run the existing testcases on different browser, by creating a fixture that can take the
  type of browser as the CLI command, and then we can supply it to the setup method, which can create the driver
  accordingly.
- This file contains PyTest HTML report settings - https://pytest-html.readthedocs.io/en/latest/user_guide.html

"""
from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key
from seleniumbase import Driver


# I am using SeleniumBase in order to bypass the cloudflare challenge - As of now only available for chrome
# For Edge and firefox - I am not able to bypass the cloudflare
# But with this structure I am keeping it for showing Cross Browsing Testing
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = Driver(uc=True)
    elif browser == 'edge':
        driver = Driver(browser=browser)
        # driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = Driver(browser=browser)
        # driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser: " + browser)

    return driver, browser


# set up the CLI argument to receive the type of browser we need the Testcase to run
def pytest_addoption(parser):
    parser.addoption('--browserArg', default='chrome', help='You can run your testcases in any one of the browsers - '
                                                            'chrome, firefox or edge')


# Gets the 'browser' value and ends it to the setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption('--browserArg')


################### PyTest HTML Report ##############################

# Hook for adding Environment information to the HTML report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "nopCommerce Automation Project"
    config.stash[metadata_key]["Module"] = "Customers"
    config.stash[metadata_key]["Environment"] = "QA"
    config.stash[metadata_key]["Tester"] = "Uthra"


# Hook for delete/modify  environment  info HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)


def pytest_html_report_title(report):
    report.title = "nopCommerce Automation - Report"
