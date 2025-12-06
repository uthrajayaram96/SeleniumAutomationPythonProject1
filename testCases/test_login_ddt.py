from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.getFilename import RenameFile
from utilities.readProperties import ReadConfig
from utilities.customLogging import Logging


class Test002Login:
    base_url = ReadConfig().get_base_url()
    file_name = ReadConfig().get_login_testdata_filename()
    logger = Logging.generate_log()

    def test_login_ddt(self, setup):
        self.logger.info('************* Start TC003_test_login_ddt *********')
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.base_url)
        assert 'nopCommerce demo store. Login' in self.driver.title
        lp = LoginPage(self.driver)

        # get user email and password from the excel file


        self.logger.info('Entering user email')
        lp.enter_user_email(self.user_email)
        self.logger.info('Entering password')
        lp.enter_login_password(self.password)
        self.logger.info('Clicking on the Login button')
        lp.click_login_btn()
        actual_title = self.driver.title
        # time.sleep(20)
        if 'Dashboard / nopCommerce administration' == actual_title:
            print(self.driver.title)
            assert True
            self.logger.info('Login Successful')
            self.logger.info('Actual title matches the expected title')
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_" + RenameFile.get_filename())
            self.logger.error('Login Failed')
            self.logger.error('Actual title does not match the expected title')
            assert False

        self.driver.quit()
        self.logger.info('************* End TC002_test_login ***********')
