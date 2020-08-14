from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver = webdriver.Chrome(executable_path='C:\\Users\\JagguMiniPC\\PycharmProjects\\PythonSelenium\\Executables\\chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    # sleep(5)
    driver.find_element_by_class_name("search-keyword").send_keys("Ca")
    sleep(5)
    # wait = WebDriverWait(driver, 5)
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.products div.product')))
    count = len(driver.find_elements_by_css_selector("div.products div.product"))
    assert count == 4
    buttons = driver.find_elements_by_xpath("//div[@class='product']//button")

    items = []
    cart = []

    for button in buttons:
        items.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
        button.click()

    print(items)
    driver.find_element_by_css_selector("img[alt='Cart']").click()
    # sleep(5)
    driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
    # sleep(5)

    cartItems = driver.find_elements_by_xpath("//div[@class='products']//p[@class='product-name']")
    for i in cartItems:
        cart.append(i.text)

    print(cart)

    assert items == cart
    driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
    driver.find_element_by_css_selector(".promoBtn").click()
    # print(driver.find_element_by_css_selector(".promo-btn-loader").text)
    print(driver.find_element_by_css_selector(".promoInfo").text)
finally:
    driver.quit()
