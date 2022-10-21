from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login is not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register_form is not presented"

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        mail.send_keys(email)
        pas1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        pas1.send_keys(password)
        pas2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        pas2.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN)
        register_btn.click()
