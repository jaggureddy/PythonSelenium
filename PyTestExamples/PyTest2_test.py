import pytest


@pytest.mark.first
def test_Test2():
    print('Second')

# py.test -v -s
# py.test -m first -v -s
# py.test -k first  -v -s
