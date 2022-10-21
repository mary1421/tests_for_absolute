import pytest, time
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

@pytest.mark.need_review
#@pytest.mark.parametrize(
#    "url_suffix",
#    [
#        f"?promo=offer{i}" for i in range(10)
#    ]
#)
def test_guest_can_add_product_to_basket(browser, \
#                                         url_suffix\
                                         ):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #product_page = ProdPage(browser, link + url_suffix)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page = ProductPage(browser, link)
    product_page.open()  # открываем страницу
    product_page.should_not_be_success_message()
    name_product = product_page.get_product_name()
    price_product = product_page.get_price_product()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_sum_basket(price_product)
    product_page.should_be_added_product(name_product)

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_basket_empty_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS)

#@pytest.mark.skip
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, '1a2S3d4F5g6H7j')
        time.sleep(5)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()  # открываем страницу
        product_page.should_not_be_success_message()
        name_product = product_page.get_product_name()
        price_product = product_page.get_price_product()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_sum_basket(price_product)
        product_page.should_be_added_product(name_product)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS)