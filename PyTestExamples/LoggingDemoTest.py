from PyTestExamples.BaseClass import BaseClass


class TestLogging(BaseClass):

    def test_loggingDemo(self, dataProvider):
        logger = self.GetLogger()
        logger.info(dataProvider)
