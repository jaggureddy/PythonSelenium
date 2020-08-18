import pytest


@pytest.mark.first
def test_Test2():
    print('Second')

# py.test -v -s
# py.test -m first -v -s
# py.test -k first  -v -s
# --html=report.html

@pytest.fixture()
def setup():
    print('Executed first')


def test_fixtureDemo(setup):
    print('Executed Next')
