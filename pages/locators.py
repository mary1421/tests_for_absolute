from selenium.webdriver.common.by import By

class BasePageLocators():
    VIRUS_CONTACT = (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[1]/label[2]/span")
    CHECKED_SUM_POLIS = (By.CSS_SELECTOR, ".slider > .on")
    #PRICE = (By.CSS_SELECTOR, "#price")
    BTN_CALCULATE = (By.NAME, "calculate")

class FillingFormLocators():
    FIO = (By.NAME, "name")
    BIRTH_DATE = (By.NAME, "dateBirth")
    PASSPORT_NUM = (By.NAME, "id")
    PASSPORT_DATE = (By.NAME, "idDate")
    ADDRESS = (By.NAME, "address")
    PHONE = (By.NAME, "phone")
    EMAIL = (By.NAME, "email")
    ADDPERSON = (By.NAME, "addPerson")
    BTN_TO_PAY = (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[2]/form/div[5]/button")

class PaymentPageLocators():
    SUM_POLIS = (By.CSS_SELECTOR, ' tui-money > span:nth-child(2)')
