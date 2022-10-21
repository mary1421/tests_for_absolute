from .locators import BasePageLocators, FillingFormLocators, PaymentPageLocators
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def predcalculate_polis(self):
        SUM_POLIS = self.browser.find_element(*BasePageLocators.CHECKED_SUM_POLIS).text
        vir_cont = self.browser.find_element(*BasePageLocators.VIRUS_CONTACT)
        vir_cont.click()
        calc_btn = self.browser.find_element(*BasePageLocators.BTN_CALCULATE)
        calc_btn.click()
        return SUM_POLIS

    def fill_form(self, fio, birth_date, passport_num, passport_date, address, phone, email, addperson):
        name = self.browser.find_element(*FillingFormLocators.FIO)
        name.send_keys(fio)
        birth = self.browser.find_element(*FillingFormLocators.BIRTH_DATE)
        birth.send_keys(birth_date)
        passp = self.browser.find_element(*FillingFormLocators.PASSPORT_NUM)
        passp.send_keys(passport_num)
        p_d = self.browser.find_element(*FillingFormLocators.PASSPORT_DATE)
        p_d.send_keys(passport_date)
        addr = self.browser.find_element(*FillingFormLocators.ADDRESS)
        addr.send_keys(address)
        ph_n = self.browser.find_element(*FillingFormLocators.PHONE)
        ph_n.send_keys(phone)
        mail = self.browser.find_element(*FillingFormLocators.EMAIL)
        mail.send_keys(email)
        add_p = self.browser.find_element(*FillingFormLocators.ADDPERSON)
        if addperson == 'ON':
            add_p.click()
        register_btn = self.browser.find_element(*FillingFormLocators.BTN_TO_PAY)
        register_btn.click()

    def go_to_pay(self):
        register_btn = self.browser.find_element(*FillingFormLocators.BTN_TO_PAY)
        register_btn.click()

    def should_be_payment_url(self):
        assert 'securepayments.tinkoff' in self.browser.current_url, "securepayments.tinkoff is not in url"

    def should_be_sum_polis(self, sum):
        text = self.browser.find_element(*PaymentPageLocators.SUM_POLIS).text
        return text
        assert self.browser.find_element(*PaymentPageLocators.SUM_POLIS).text == sum, "Sum is wrong"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
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

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True