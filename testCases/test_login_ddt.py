from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.DashboardPage import DashboardPage
from utilities.getFilename import RenameFile
from utilities.readProperties import ReadConfig
from utilities.customLogging import Logging
from utilities.DataProviders import DataProviders


class Test002Login:
    base_url = ReadConfig().get_base_url()
    file_name = ReadConfig().get_login_testdata_filename()
    logger = Logging.generate_log()

    def test_login_ddt(self, setup):
        self.logger.info('************* Start TC002_test_login_ddt *********')
        self.driver, browser = setup
        self.driver.implicitly_wait(20)

        # bypass the cloudflare challenge
        if browser == 'chrome':
            self.driver.uc_open_with_reconnect(self.base_url, 4)
        else:
            self.driver.get(self.base_url)

        assert 'nopCommerce demo store. Login' in self.driver.title
        lp = LoginPage(self.driver)
        dp = DashboardPage(self.driver)

        # get user email and password from the Excel file
        test_data = DataProviders.get_test_data(self.file_name)

        for data in test_data:

            self.logger.info('Entering user email')
            lp.enter_user_email(data[0])
            self.logger.info('Entering password')
            lp.enter_login_password(data[1])
            self.logger.info('Clicking on the Login button')
            lp.click_login_btn()

            # bypass the cloudflare challenge
            if browser == 'chrome':
                self.driver.uc_gui_click_captcha()

            actual_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            # If login was successful, and the expected result is pass, the TC is considered pass
            if exp_title == actual_title:
                if data[2] == 'Pass':
                    print(self.driver.title)
                    self.logger.info('Login Successful')
                    self.logger.info('Actual title matches the expected title')
                    dp.click_logout_btn()
                    self.logger.info('Logging out....')
                    assert True
                else:
                    # TC failed as we cannot log in with correct credentials
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_login_" + RenameFile.get_filename())
                    self.logger.error('Login Failed')
                    self.logger.error('Actual title does not match the expected title')
                    assert False

            else:
                if data[2] == 'Fail':
                    self.logger.info('Cannot log in with incorrect credentials.')
                    assert True
                else:
                    self.logger.error('Can log in with incorrect credentials.')
                    dp.click_logout_btn()
                    self.logger.info('Logging out....')
                    assert False

        self.driver.quit()
        self.logger.info('************* End TC003_test_login_ddt ***********')
