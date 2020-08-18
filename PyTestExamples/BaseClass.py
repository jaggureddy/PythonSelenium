import logging
import pytest


@pytest.mark.usefixtures('setup')
class BaseClass:

    def GetLogger(self):
        logger = logging.getLogger(__name__)
        file = logging.FileHandler('LogFile.log')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file.setFormatter(formatter)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger
