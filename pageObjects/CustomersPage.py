"""
Customers class contains all the page objects/fields related to the Customers option in the dashboard page like:
Customers, Customer roles, Online customers, Vendors, Activity logs, Activity types etc
"""

from selenium.webdriver.common.by import By
from selenium import webdriver


class CustomersPage:
    customers_sub_option = "//a[@href='/Admin/Customer/List']"
    add_new_customers_btn = "//a[@href='/Admin/Customer/Create']"

    def __init__(self, driver):
        self.driver = driver

    def click_customers_sub_option(self):
        self.driver.find_element(By.XPATH, self.customers_sub_option).click()

    def click_add_new_customers_btn(self):
        self.driver.find_element(By.XPATH, self.add_new_customers_btn).click()
