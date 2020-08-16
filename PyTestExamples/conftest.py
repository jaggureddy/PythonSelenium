import pytest


@pytest.fixture(scope='class')
def setup():
    print('Executed first')
    yield
    print('Executed Last')


@pytest.fixture()
def dataProvider():
    print('Data Load')
    return ['Jaggu', 'Reddy']


@pytest.fixture(params=['Chrome', 'IE', 'Firefox'])
def crossBrowser(request):
    return request.param
