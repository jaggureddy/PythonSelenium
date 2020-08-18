import logging


def test_LoggingDemo():
    logger = logging.getLogger(__name__)

    file = logging.FileHandler('LogFile.log')
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')

    file.setFormatter(formatter)
    logger.addHandler(file)
    logger.setLevel(logging.INFO)

    logger.debug('Debug')
    logger.info('Info')
    logger.warning('Warning')
    logger.error('Error')
    logger.critical('Critical')
