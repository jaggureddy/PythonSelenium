import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def setup(request):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path='C:\\Users\\JagguMiniPC\\PycharmProjects\\PythonSelenium\\Executables\\chromedriver.exe', options=chromeOptions)
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture()
def dataProvider():
    print('Data Load')
    return ['Jaggu', 'Reddy']


@pytest.fixture(params=['Chrome', 'IE', 'Firefox'])
def crossBrowser(request):
    return request.param
