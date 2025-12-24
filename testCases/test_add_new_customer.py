import pytest
from selenium import webdriver
from pageObjects.CustomersPage import CustomersPage
from pageObjects.AddNewCustomerPage import AddNewCustomerPage
from pageObjects.DashboardPage import DashboardPage
from pageObjects.LoginPage import LoginPage
from utilities.getFilename import RenameFile
from utilities.readProperties import ReadConfig
from utilities.customLogging import Logging
from utilities.GenerateTestData import GenerateTestData
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Test003AddNewCustomer:
    base_url = ReadConfig().get_base_url()
    user_email = ReadConfig().get_user_email()
    password = ReadConfig().get_password()
    logger = Logging.generate_log()

    def test_add_new_customer(self, setup):
        self.logger.info('************* Start TC003_test_add_new_customer *********')

        self.driver, browser = setup

        try:
            self.driver.implicitly_wait(20)

            # bypass the cloudflare challenge
            if browser == 'chrome':
                self.driver.uc_open_with_reconnect(self.base_url, 4)
            else:
                self.driver.get(self.base_url)

            assert 'nopCommerce demo store. Login' in self.driver.title

            self.logger.info("\n--- Logging in ---")

            lp = LoginPage(self.driver)
            self.logger.info('Entering user email')
            lp.enter_user_email(self.user_email)
            self.logger.info('Entering password')
            lp.enter_login_password(self.password)
            self.logger.info('Clicking on the Login button')
            lp.click_login_btn()

            # bypass the cloudflare challenge
            if browser == 'chrome':
                self.driver.uc_gui_click_captcha()

            dp = DashboardPage(self.driver)
            cp = CustomersPage(self.driver)
            acp = AddNewCustomerPage(self.driver)

            self.logger.info("\n--- Clicking on Customers option from the dashboard ---")
            dp.click_customers_menu()

            self.logger.info("\n--- Clicking on Customers sub option under Customers option ---")
            cp.click_customers_sub_option()

            assert 'Customers / nopCommerce administration' in self.driver.title

            self.logger.info("\n--- Adding/creating new customer details ---")
            cp.click_add_new_customers_btn()

            acp.enter_customer_email(GenerateTestData.generate_email())
            acp.enter_customer_password(GenerateTestData.generate_password())
            acp.enter_customer_first_name(GenerateTestData.generate_first_name())
            acp.enter_customer_last_name(GenerateTestData.generate_last_name())
            acp.select_customer_gender(GenerateTestData.generate_gender())
            acp.enter_customer_company_name(GenerateTestData.generate_company_name())

            role = ''
            while role not in ['Guests', 'Registered']:
                role = GenerateTestData.generate_customer_roles()
            print(role)
            acp.select_customer_roles(role)

            acp.select_manager_of_vendor(GenerateTestData.generate_manager_of_vendor())
            acp.enter_admin_comments(GenerateTestData.generate_comments())
            acp.click_save_btn()

            if 'The new customer has been added successfully.' == acp.get_confirmation_message():
                print(acp.get_confirmation_message())
                assert True
                self.logger.info('Added new customer details!')
                self.logger.info('TC003_test_add_new_customer passed!')
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_add_new_customer_" + RenameFile.get_filename())
                self.logger.error("Couldn't add new customer details!")
                self.logger.error('TC003_test_add_new_customer failed!')
                assert False

            self.logger.info("\n--- Logging out ---")
            dp.click_logout_btn()

        except TimeoutException as te:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_new_customer_" + RenameFile.get_filename())
            self.logger.error("Couldn't add new customer details!")
            self.logger.error('TC003_test_add_new_customer failed!')
            print(te)
            assert False

        except NoSuchElementException as se:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_new_customer_" + RenameFile.get_filename())
            self.logger.error("Couldn't add new customer details!")
            self.logger.error('TC003_test_add_new_customer failed!')
            print(se)
            assert False

        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_new_customer_" + RenameFile.get_filename())
            self.logger.error("Couldn't add new customer details!")
            self.logger.error('TC003_test_add_new_customer failed!')
            print(e)
            assert False

        finally:
            self.driver.quit()
            self.logger.info('************* End TC003_test_add_new_customer ***********')







