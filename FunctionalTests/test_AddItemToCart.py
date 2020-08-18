from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Utilities.BaseClass import BaseClass


class TestAddItemToCart(BaseClass):

    def test_AddItemToCart(self):
        self.driver.find_element_by_xpath("//a[text()='Shop']").click()
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for product in products:
            name = product.find_element_by_xpath("div/h4/a").text
            if name == "Blackberry":
                product.find_element_by_xpath("div/button").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Checkout')]").click()
        sleep(10)
        checkout = self.driver.find_element_by_xpath("//button[@class='btn btn-success']")
        self.driver.execute_script("arguments[0].click();", checkout)
        wait = WebDriverWait(self.driver, 10)
        # self.driver.get_screenshot_as_file('screen.png')
        wait.until(expected_conditions.presence_of_element_located(By.ID, 'country'))
        self.driver.find_element_by_id("country").send_keys("Ind")
        wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT, "India"))
        self.driver.find_element_by_link_text('India').click()
        sleep(5)
