# Includes the login testcase - happy path


from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.getFilename import RenameFile
from utilities.readProperties import ReadConfig
from utilities.customLogging import Logging


class Test001Login:
    base_url = ReadConfig().get_base_url()
    user_email = ReadConfig().get_user_email()
    password = ReadConfig().get_password()
    logger = Logging.generate_log()

    def test_homepage_title(self, setup):
        self.logger.info('************* Start TC001_test_homepage_title *********')
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.base_url)
        if 'nopCommerce demo store. Login' == self.driver.title:
            print(self.driver.title)
            assert True
            self.logger.info('Actual title matches the expected title')
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title_" + RenameFile.get_filename())
            self.logger.error('Actual title does not match the expected title')
            assert False

        self.driver.quit()
        self.logger.info('************* End TC001_test_homepage_title ***********')

    def test_login(self, setup):
        self.logger.info('************* Start TC002_test_login *********')
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.base_url)
        assert 'nopCommerce demo store. Login' in self.driver.title
        lp = LoginPage(self.driver)
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
