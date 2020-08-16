import pytest


def test_fixtureDemo(setup):
    print('Executed Next')


@pytest.mark.usefixtures('setup', 'dataProvider')
class TestFixtures:
    def test_Demo1(self):
        print('Demo 1')

    def test_Demo2(self):
        print('Demo 2')

    def test_TestData(self, dataProvider):
        print(dataProvider)
