import pytest, time
from .pages.main_page import MainPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        link = "https://old.absolutins.ru/kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/zashchita-ot-virusa/"
        page = MainPage(browser, link)
        page.open()
        sum_polis = page.predcalculate_polis()
        fio = "Иванов Иван Иванович"
        birth_date = '12.04.1999'
        passport_num = '5004 678901'
        passport_date = '12.05.2016'
        address = 'г Москва, ул Академика Королева, влд 2А '
        phone = '9034567788'
        email = 'mail7531@gmail.com'
        addperson = "ON"
        page.fill_form(fio, birth_date, passport_num, passport_date, address, phone, email, addperson)
        page.go_to_pay()
        time.sleep(20)
        page.should_be_payment_url()
        page.should_be_sum_polis(sum_polis)
'''
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_basket_empty_message()
'''
