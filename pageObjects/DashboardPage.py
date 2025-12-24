from selenium.webdriver.common.by import By
from selenium import webdriver


class DashboardPage:
    logout_button_lnkText = 'Logout'
    customers_menu_option = "//a[@href='#']//p[contains(text(),'Customers')]"

    def __init__(self, driver):
        self.driver = driver

    def click_logout_btn(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_button_lnkText).click()

    def click_customers_menu(self):
        self.driver.find_element(By.XPATH, self.customers_menu_option).click()



