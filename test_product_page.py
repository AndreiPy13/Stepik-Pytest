import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
from faker import Faker


#ПРОМО АКЦИЯ
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks = pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_should_see_login_link(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket_PROMO()
    #time.sleep(120)


#ПРОМО NEWYEAR
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link, 5)
    page.open()
    page.test_guest_can_add_product_to_basket_NewYear()



#ОТРИЦАТЕЛЬНЫЕ ПРОВЕРКИ
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
@pytest.mark.xfail
#1 - не проходит(так и надо)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_to_add_in_basket()
    page.should_not_be_success_message()

#2 - проходит
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

#3 - не проходит(так и надо)
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_to_add_in_basket()
    page.should_dissapear_of_success_message()

#Открываем страницу с товаром -- корзина -- пустота
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(browser, link)
    page.open()
    page.product_in_basket()

#ГОСТЬ МОЖЕТ ПЕРЕЙТИ НА СТРАНИЦУ ЛОГИ СО СТРАНИЦЫ - Х
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

#ПРОВЕРКА ПОЛЕЙ НА СТР. ВХОДА
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page=LoginPage(browser,link)
    page.open()
    page.go_to_login_page() #перейти на страницу с регистрацией
    page.should_be_login_page() #проверка полей регистрации и входа

#ПРОВЕРКА НА РЕГИСТРАЦИЮ ПОЛЬЗОВАТЕЛЯ + ДЕЙСТВИЯ
@pytest.mark.registration_guest
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        fake = Faker()
        email = fake.email()
        password = '123456hhhd'
        page=LoginPage(browser,link)
        page.open()
        page.go_to_login_page() #перейти на страницу с регистрацией
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link, 5)
        page.open()
        page.test_guest_can_add_product_to_basket_PROMO()

#pytest -s -v --tb=line --language=en test_product_page.py

#pytest -s -v --tb=line --language=en test_product_page.py -m registration_guest

#pytest -v --tb=line --language=en -m need_review