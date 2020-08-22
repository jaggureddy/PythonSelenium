import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass:

    def verifyLinkPresence(self, by, text):
        wait = WebDriverWait(self.driver, 10)
        if by == 'ID':
            wait.until(expected_conditions.presence_of_element_located((By.ID, text)))
        elif by == 'LINKTEXT':
            wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
        else:
            pass

    def GetLogger(self):
        logger = logging.getLogger(__name__)
        file = logging.FileHandler('LogFile.log')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file.setFormatter(formatter)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger

# py.test --browser_name firefox
