from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
import math
import pytest


class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket_PROMO(self):
        self.promo_in_URL_offer()
        self.click_to_add_in_basket()
        self.math_answer()
        self.control_text()
        self.control_price()


    def test_guest_can_add_product_to_basket_NewYear(self):
        self.promo_in_URL_NewYear()
        self.click_to_add_in_basket()
        self.math_answer()
        self.control_text()
        self.control_price()

    def promo_in_URL_offer(self):
        assert '?promo=offer' in self.browser.current_url, 'in URL not found promo offer'
        

    def click_to_add_in_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        button.click()
      

    def math_answer(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def promo_in_URL_NewYear(self):
        assert '?promo=newYear' in self.browser.current_url, 'in URL not found promo newYear'

    def control_text(self):
        name_in_notice = self.browser.find_element(*ProductPageLocators.NAME_IN_NOTIFICATION).text
        name_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        assert name_in_notice == name_product, "Name product in notification is incorrect"


    def control_price(self):
        price_in_notice = self.browser.find_element(*ProductPageLocators.PRICE_IN_NOTIFICATION).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_in_notice == price_product


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The success message does not disappear"
