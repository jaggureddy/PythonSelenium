import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption('browser_name')
    if browser == 'chrome':
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--start-maximized")
        driver = webdriver.Chrome(executable_path='C:\\Users\\JagguMiniPC\\PycharmProjects\\PythonSelenium\\Executables\\chromedriver.exe', options=chromeOptions)
        driver.implicitly_wait(10)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='C:\\Users\\JagguMiniPC\\PycharmProjects\\PythonSelenium\\Executables\\geckodriver.exe')
    else:
        pass

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

