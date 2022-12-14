from .locators import (
    BasePageLocators,
    FillingFormLocators,
    PaymentPageLocators,
    EmptyLocators,
)
import time


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def predcalculate_polis(self, str_sum):
        if str_sum == "100 000":
            sum_slider = self.browser.find_element(*BasePageLocators.SLIDER_SUM)
            sum_slider.click()
        vir_cont = self.browser.find_element(*BasePageLocators.VIRUS_CONTACT)
        vir_cont.click()

    def go_to_filling(self):
        calc_btn = self.browser.find_element(*BasePageLocators.BTN_CALCULATE)
        calc_btn.click()

    def fill_form(
        self, fio, birth_date, passport_num, passport_date, address, phone, email
    ):
        name = self.browser.find_element(*FillingFormLocators.FIO)
        name.send_keys(fio)
        birth = self.browser.find_element(*FillingFormLocators.BIRTH_DATE)
        birth.click()
        time.sleep(1)
        birth.send_keys(birth_date)
        passp = self.browser.find_element(*FillingFormLocators.PASSPORT_NUM)
        passp.click()
        passp.send_keys(passport_num)
        p_d = self.browser.find_element(*FillingFormLocators.PASSPORT_DATE)
        p_d.click()
        time.sleep(1)
        p_d.send_keys(passport_date)
        addr = self.browser.find_element(*FillingFormLocators.ADDRESS)
        addr.click()
        addr.send_keys(address)
        ph_n = self.browser.find_element(*FillingFormLocators.PHONE)
        ph_n.send_keys(phone)
        mail = self.browser.find_element(*FillingFormLocators.EMAIL)
        mail.send_keys(email)
        # add_p = self.browser.find_element(*FillingFormLocators.ADDPERSON)
        # if addperson == 'ON':
        #    add_p.click()

    def go_to_pay(self):
        register_btn = self.browser.find_element(*FillingFormLocators.BTN_TO_PAY)
        time.sleep(10)
        register_btn.click()

    def should_be_payment_page(self, sum):
        self.should_be_payment_url()
        self.should_be_sum_polis_in_payment(sum)

    def should_be_payment_url(self):
        current_url = self.browser.current_url
        assert "securepayments.tinkoff" in current_url, (
            "?????????????????? securepayments.tinkoff ???? ?????????????? ?? url"
            ", ?????????????? url - '{current_url}'"
        )

    def should_not_be_payment_url(self):
        assert (
            "securepayments.tinkoff" not in self.browser.current_url
        ), "?????????????????? securepayments.tinkoff ?????????????? ?? url"

    def should_be_sum_polis_in_payment(self, sum):
        assert (
            self.browser.find_element(*PaymentPageLocators.SUM_POLIS).text == sum[:5]
        ), "???????????????? ?????????? ????????????."

    def should_be_sums(self, str_sum):
        if str_sum == "100 000":
            sum_polis = "1 500 ???"
            hosp = "500"
        else:
            sum_polis = "5 000 ???"
            hosp = "1 500"
        if (
            self.browser.find_elements(*BasePageLocators.HOSP)[0].get_attribute(
                "hidden"
            )
            == "true"
        ):
            hosp_sum = self.browser.find_elements(*BasePageLocators.HOSP)[1].text
        else:
            hosp_sum = self.browser.find_elements(*BasePageLocators.HOSP)[0].text
        assert hosp_sum == hosp, "???????????????? ?????????????????? ?????? ????????????????????????????."
        a = self.browser.find_elements(*BasePageLocators.PARENT_PRICE)
        b = self.browser.find_elements(*BasePageLocators.PRICE)
        if (
            self.browser.find_elements(*BasePageLocators.PARENT_PRICE)[0].get_attribute(
                "hidden"
            )
            == "true"
        ):
            price = self.browser.find_elements(*BasePageLocators.PRICE)[
                1
            ].get_attribute("placeholder")
        else:
            price = self.browser.find_elements(*BasePageLocators.PRICE)[
                0
            ].get_attribute("placeholder")
        assert price == sum_polis, "???????????????? ?????????????????? ????????????."
        return price

    def should_empty_message(self, par):
        EMPTY_MES = [
            "???? ?????????????? ??????????????.",
            "???? ?????????????? ???????? ????????????????.",
            "???? ?????????????? ??????????/?????????? ????????????????.",
            "???? ?????????????? ???????? ???????????? ????????????????.",
            "???? ???????????? ?????????? ??????????????????????.",
            "???? ???????????? ?????????? ????????????????.",
            "???? ???????????? E-Mail.",
        ]
        assert (
            self.browser.find_element(*EmptyLocators.EMPTY_PARS[par]).text
            == EMPTY_MES[par]
        ), "Message is wrong or not present"
