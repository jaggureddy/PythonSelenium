from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from Pages.CheckOutPage import CheckOutPage
from Pages.Confirmpage import ConfirmPage
from Pages.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestAddItemToCart(BaseClass):

    def test_AddItemToCart(self):
        homePage = HomePage(self.driver)
        checkOutPage = CheckOutPage(self.driver)
        confirmPage = ConfirmPage(self.driver)

        # self.driver.find_element_by_xpath("//a[text()='Shop']").click()
        homePage.shopItems().click()

        # products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        products = checkOutPage.getProducts()

        # for product in products:
        #     name = product.find_element_by_xpath("div/h4/a").text
        #     if name == "Blackberry":
        #         product.find_element_by_xpath("div/button").click()
        products.click()

        self.driver.execute_script("window.scrollBy(0,-1500);")
        # self.driver.find_element_by_xpath("//a[contains(text(),'Checkout')]").click()
        checkOutPage.selectCheckout().click()

        sleep(10)
        # checkout = self.driver.find_element_by_xpath("//button[@class='btn btn-success']")
        checkout = confirmPage.selectCheckout()
        self.driver.execute_script("arguments[0].click();", checkout)
        sleep(10)

        # wait = WebDriverWait(self.driver, 10)
        # self.driver.get_screenshot_as_file('screen.png')
        # wait.until(expected_conditions.presence_of_element_located(By.ID, 'country'))
        self.verifyLinkPresence('ID', 'country')

        self.driver.find_element_by_id("country").send_keys("Ind")
        # wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT, "India"))
        self.verifyLinkPresence('LINKTEXT', 'India')
        self.driver.find_element_by_link_text('India').click()
        sleep(5)
