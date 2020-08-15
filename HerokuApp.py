from selenium import webdriver


try:
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--start-maximized")
    chromeOptions.add_argument('headless')

    driver = webdriver.Chrome(executable_path='C:\\Users\\JagguMiniPC\\PycharmProjects\\PythonSelenium\\Executables\\chromedriver.exe', options=chromeOptions)
    # driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://the-internet.herokuapp.com/')
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    inputLink = driver.find_element_by_xpath('//*[@id="content"]/ul/li[27]/a')
    # driver.find_element_by_xpath('//*[@id="content"]/ul/li[27]/a').click()
    driver.execute_script("arguments[0].click();", inputLink)
    driver.find_element_by_xpath("//input[@type='number']").send_keys("10")
    print(driver.find_element_by_xpath("//input[@type='number']").get_attribute('value'))
    print(driver.execute_script("return document.getElementsByTagName('input')[0].value"))
finally:
    driver.quit()

