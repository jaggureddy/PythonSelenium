from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:\\Users\\JagguMiniPC\\PycharmProjects\\PythonSelenium\\Executables\\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='C:\\Users\\JagguMiniPC\\PycharmProjects\\PythonSelenium\\Executables\\geckodriver.exe')
driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5000)
print(driver.title)
# driver.current_url
# driver.refresh()
# driver.back()
driver.find_element_by_css_selector("input[name='name']").send_keys("J")
driver.find_element_by_name("email").send_keys("R")
driver.find_element_by_id("exampleCheck1").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")

driver.find_element_by_xpath("//input[@type='submit']").click()
driver.quit()


