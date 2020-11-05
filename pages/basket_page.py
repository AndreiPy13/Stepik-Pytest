from .base_page import BasePage
from .locators import BasketPageLocators
import time


class BasketPage(BasePage):
    def product_in_basket(self):
        self.click_on_the_shopping_cart()
        self.text_in_basket_when_no_products()
        self.empty_basket()

    def click_on_the_shopping_cart(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BUTTON_BASKET)
        basket_button.click()
        time.sleep(5)


    def text_in_basket_when_no_products(self):
        text = self.browser.find_element(*BasketPageLocators.BUTTON_0_TEXT).text
        assert text == 'Ваша корзина пуста Продолжить покупки'


    def empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCTS), \
            "There are products in the shopping cart"