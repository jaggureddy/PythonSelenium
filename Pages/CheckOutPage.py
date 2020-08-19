from selenium.webdriver.common.by import By


class CheckOutPage:
    products = (By.XPATH, "//div[@class='card h-100']")
    checkout = (By.XPATH, "//a[contains(text(),'Checkout')]")

    def __init__(self, driver):
        self.driver = driver

    def getProducts(self):
        products = self.driver.find_elements(*CheckOutPage.products)
        for product in products:
            name = product.find_element_by_xpath("div/h4/a").text
            if name == "Blackberry":
                return product.find_element_by_xpath("div/button")

    def selectCheckout(self):
        return self.driver.find_element(*CheckOutPage.checkout)
