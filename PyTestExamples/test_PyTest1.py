import pytest


@pytest.mark.first
@pytest.mark.skip
def test_first():
    msg = 'Hello'
    assert msg == 'Hi', 'Test failed'


@pytest.mark.second
def test_second():
    print('S2')


@pytest.mark.xfail
def test_second1():
    print('S2')


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
