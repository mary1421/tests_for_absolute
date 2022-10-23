from .locators import BasePageLocators, FillingFormLocators, PaymentPageLocators, EmptyLocators
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math, time

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

    def fill_form(self, fio, birth_date, passport_num, passport_date, address, phone, email):
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
        #add_p = self.browser.find_element(*FillingFormLocators.ADDPERSON)
        #if addperson == 'ON':
        #    add_p.click()

    def go_to_pay(self):
        register_btn = self.browser.find_element(*FillingFormLocators.BTN_TO_PAY)
        time.sleep(5)
        register_btn.click()

    def should_be_payment_page(self, sum):
        self.should_be_payment_url()
        self.should_be_sum_polis(sum)

    def should_be_payment_url(self):
        assert 'securepayments.tinkoff' in self.browser.current_url, "Подстрока securepayments.tinkoff не найдена в url"\
                                                                     ", текущий url - {self.browser.current_url}"

    def should_not_be_payment_url(self):
        assert 'securepayments.tinkoff' not in self.browser.current_url, "Подстрока securepayments.tinkoff найдена в url"

    def should_be_sum_polis(self, sum):
        if sum == "1 500":
            sum_polis = "5 000"
        else:
            sum_polis = "1 500"
        assert self.browser.find_element(*PaymentPageLocators.SUM_POLIS).text == sum_polis, "Неверная сумма полиса."
        #"Ожидается сумма", {sum_polis}, ", Текущая сумма - ", /
        #self.browser.find_element(*PaymentPageLocators.SUM_POLIS).text

    def should_empty_message(self, par):
        EMPTY_MES = ["Не указана фамилия.", "Не указана дата рождения.", "Не указаны серия/номер паспорта.",\
                     "Не указаны дата выдачи паспорта.", "Не указан адрес регистрации.", "Не указан номер телефона.",\
                     "Не указан E-Mail."]
        assert self.browser.find_element(*EmptyLocators.EMPTY_PARS[par]).text == EMPTY_MES[par], \
            "Message is wrong or not present"

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