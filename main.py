from selenium import webdriver


driver = webdriver.Chrome(executable_path='C:\\Users\\JagguMiniPC\\PycharmProjects\\PythonSelenium\\Executables\\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='C:\\Users\\JagguMiniPC\\PycharmProjects\\PythonSelenium\\Executables\\geckodriver.exe')



driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5000)
print(driver.title)
driver.current_url
driver.refresh()
# driver.back()
driver.quit()


