from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_NAME_FORM = (By.CSS_SELECTOR, "#id_login-username")
	LOGIN_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_login-password")
	REGISTRATION_EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTRATION_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
	REGISTRATION_RETURN_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password2")