# The Login Page contains all the page objects found in the login page

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    #Locators
    user_email_id = 'Email'
    user_password_id = 'Password'
    login_button_xpath = '//button[contains(@class,"login-button")]'

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def enter_user_email(self, email):
        self.driver.find_element(By.ID, self.user_email_id).clear()
        self.driver.find_element(By.ID, self.user_email_id).send_keys(email)

    def enter_login_password(self, password):
        self.driver.find_element(By.ID, self.user_password_id).clear()
        self.driver.find_element(By.ID, self.user_password_id).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()



