from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
	LOGIN_NAME_FORM = (By.CSS_SELECTOR, "#id_login-username")
	LOGIN_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_login-password")
	REGISTRATION_EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTRATION_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
	REGISTRATION_RETURN_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
	BASKET_FORM = (By.CSS_SELECTOR, ".btn-add-to-basket")
	NAME_IN_NOTIFICATION = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
	NAME_OF_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
	PRICE_IN_NOTIFICATION = (By.CSS_SELECTOR, ".alert-info.fade.in > div > p:nth-child(1) > strong") 
	PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > p.price_color")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasketPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    BUTTON_0_TEXT = (By.XPATH, '//*[@id="content_inner"]/p')
    PRODUCTS = (By.CSS_SELECTOR, "#content_inner")