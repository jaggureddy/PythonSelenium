import pytest


@pytest.mark.usefixtures('setup')
class BaseClass:
    pass


# py.test --browser_name firefox
