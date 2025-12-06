"""
- This file contains setup method that created a common webdriver object and returns it.
- This object can be used by other testcases class, by calling the setup() method
- We have the option to run the existing testcases on different browser, by creating a fixture that can take the
  type of browser as the CLI command, and then we can supply it to the setup method, which can create the driver
  accordingly.
- This file contains PyTest HTML report settings - https://pytest-html.readthedocs.io/en/latest/user_guide.html

"""
from selenium import webdriver
import undetected_chromedriver as uc
import pytest
from pytest_metadata.plugin import metadata_key


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        # driver = uc.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        print('Wrong value passed to the browser argument')
        driver = None
    return driver


# set up the CLI argument to receive the type of browser we need the Testcase to run
def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='You can run your testcases in any one of the browsers - '
                                                         'chrome, firefox or edge')


# Gets the 'browser' value and ends it to the setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


################### PyTest HTML Report ##############################

# Hook for adding Environment information to the HTML report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "nopCommerce Automation Project"
    config.stash[metadata_key]["Module"] = "Customers"
    config.stash[metadata_key]["Environment"] = "QA"
    config.stash[metadata_key]["Tester"] = "Uthra"


# Hook for delete/modify  environment  info HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)


def pytest_html_report_title(report):
    report.title = "nopCommerce Automation - Report"
