from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'in URL not found login word'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_NAME_FORM), 'Not found name_form in login'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FORM), 'Not found password_form in login'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_FORM), 'Not found email_form in registration'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_FORM), 'Not found first password_form in registration'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_RETURN_PASSWORD_FORM), 'Not found second password_form in registration'