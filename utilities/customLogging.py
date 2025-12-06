# This utility file helps create custom log file

import logging
from logging.handlers import RotatingFileHandler


class Logging:
    @staticmethod
    def generate_log():
        # logging.basicConfig(filename='.\\Logs\\automation.log',
        #                     format='[%(asctime)s] %(levelname)s - %(message)s',
        #                     datefmt='%Y-%m-%d %H:%M:%S')

        logger = logging.getLogger()
        # file_handler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')

        # This will roll over after 50000 bytes and can rename upto 10 files, so we will have
        # automation.log.1,...,automation.log.10

        file_handler = RotatingFileHandler(
            filename='.\\Logs\\automation.log',
            maxBytes=50_000,
            backupCount=10
        )
        file_formatter = logging.Formatter(fmt='[%(asctime)s] %(levelname)s - %(message)s',
                                           datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
