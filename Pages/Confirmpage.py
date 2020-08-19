from selenium.webdriver.common.by import By


class ConfirmPage:
    checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def selectCheckout(self):
        return self.driver.find_element(*ConfirmPage.checkout)
