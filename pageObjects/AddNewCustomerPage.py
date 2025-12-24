"""
AddNewCustomer class contains all the page objects/fields to add a new customer after login

"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddNewCustomerPage:
    customer_email_name = 'Email'
    customer_password_id = 'Password'
    customer_first_name_id = 'FirstName'
    customer_last_name_id = 'LastName'
    customer_gender_id = ['Gender_Male', 'Gender_Female']
    customer_company_name = 'Company'
    customer_is_tax_exempt_id = 'IsTaxExempt'
    customer_roles_id = 'SelectedCustomerRoleIds'
    customer_roles_remove_default_xpath = '//span[@class="select2-selection__choice__remove"]'
    customer_manager_of_vendor_xpath = "//span[@class='select2-selection select2-selection--single']"
    vendor_list_xpath = "//ul[contains(@class,'select2-results__options')]//li"
    customer_admin_comment_id = "AdminComment"
    save_btn_name = 'save'
    save_and_continue_btn_name = 'save-continue'
    confirmation_msg_xpath = "//span[contains(text(),'The new customer has been added successfully.')]"

    def __init__(self, driver):
        self.driver = driver

    def enter_customer_email(self, email):
        self.driver.find_element(By.NAME, self.customer_email_name).send_keys(email)

    def enter_customer_password(self, password):
        self.driver.find_element(By.ID, self.customer_password_id).send_keys(password)

    def enter_customer_first_name(self, first_name):
        self.driver.find_element(By.ID, self.customer_first_name_id).send_keys(first_name)

    def enter_customer_last_name(self, last_name):
        self.driver.find_element(By.ID, self.customer_last_name_id).send_keys(last_name)

    def select_customer_gender(self, gender):
        if gender.lower() == 'male':
            self.driver.find_element(By.ID, self.customer_gender_id[0]).click()
        elif gender.lower() == 'female':
            self.driver.find_element(By.ID, self.customer_gender_id[1]).click()

    def enter_customer_company_name(self, company):
        self.driver.find_element(By.NAME, self.customer_company_name).send_keys(company)

    def click_is_tax_exempt(self):
        self.driver.find_element(By.ID, self.click_is_tax_exempt).click()

    def select_customer_roles(self, customer_role):
        self.driver.find_element(By.XPATH, self.customer_roles_remove_default_xpath).click()
        select_obj = Select(self.driver.find_element(By.ID, self.customer_roles_id))
        select_obj.select_by_visible_text(customer_role)

    def select_manager_of_vendor(self, manager_vendor):
        # print(manager_vendor)
        self.driver.find_element(By.XPATH, self.customer_manager_of_vendor_xpath).click()
        list_vendors = self.driver.find_elements(By.XPATH, self.vendor_list_xpath)
        for v in list_vendors:
            # print(v.text)
            if manager_vendor == v.text:
                v.click()
                break

    def enter_admin_comments(self, comments):
        self.driver.find_element(By.ID, self.customer_admin_comment_id).send_keys(comments)

    def click_save_btn(self):
        self.driver.find_element(By.NAME, self.save_btn_name).click()

    def click_save_and_continue_btn(self):
        self.driver.find_element(By.NAME, self.save_and_continue_btn_name).click()

    def get_confirmation_message(self):
        wait = WebDriverWait(self.driver, 10)
        success_message = wait.until(EC.visibility_of_element_located((By.XPATH, self.confirmation_msg_xpath)))
        return success_message.text
