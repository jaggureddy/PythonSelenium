from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

try:
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path='C:\\Users\\JagguMiniPC\\PycharmProjects\\PythonSelenium\\Executables\\chromedriver.exe', options=chromeOptions)
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.find_element_by_xpath("//a[text()='Shop']").click()
    products = driver.find_elements_by_xpath("//div[@class='card h-100']")
    for product in products:
        name = product.find_element_by_xpath("div/h4/a").text
        if name == "Blackberry":
            product.find_element_by_xpath("div/button").click()
    driver.find_element_by_xpath("//a[contains(text(),'Checkout')]").click()
    sleep(10)
    checkout = driver.find_element_by_xpath("//button[@class='btn btn-success']")
    driver.execute_script("arguments[0].click();", checkout)
    wait = WebDriverWait(driver, 10)
    driver.get_screenshot_as_file('screen.png')
    wait.until(expected_conditions.presence_of_element_located(By.ID, 'country'))
    driver.find_element_by_id("country").send_keys("Ind")
    wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT, "India"))
    driver.find_element_by_link_text('India').click()
    sleep(5)
finally:
    driver.quit()
