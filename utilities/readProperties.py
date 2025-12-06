# This utility file contains helper methods to read data from the 'config.ini' file
# We can use the package 'configparser'

import configparser

# create an object of the class RawConfigParser()
config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


# create a class that returns the data from the 'config.ini' file

class ReadConfig:
    @staticmethod
    def get_base_url():
        url = config.get('common data', 'base_url')
        return url

    @staticmethod
    def get_user_email():
        email = config.get('common data', 'user_email')
        return email

    @staticmethod
    def get_password():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def get_login_testdata_filename():
        file_name = config.get('common data', 'login_test_data_file_name')
        return file_name
