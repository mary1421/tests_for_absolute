from selenium.webdriver.common.by import By

class BasePageLocators():
    VIRUS_CONTACT = (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[1]/label[2]/span")
    PARENT_PRICE = (By.CSS_SELECTOR, ".option-description")
    PRICE = (By.CSS_SELECTOR, "#price")
    SLIDER_SUM = (By.CSS_SELECTOR, ".slider")
    HOSP = (By.CSS_SELECTOR, ".hospitalization")
    BTN_CALCULATE = (By.NAME, "calculate")

class FillingFormLocators():
    FIO = (By.NAME, "name")
    DATEPICKER = (By.CSS_SELECTOR, ".datepicker")
    DATEPICKER_YEARS = (By.CSS_SELECTOR, ".year")
    DATEPICKER_MONTH = (By.CSS_SELECTOR, ".month")
    DATEPICKER_DAYS = (By.CSS_SELECTOR, ".days")
    BIRTH_DATE = (By.CSS_SELECTOR, "#dateBirth")
    PASSPORT_NUM = (By.NAME, "id")
    PASSPORT_DATE = (By.NAME, "idDate")
    ADDRESS = (By.NAME, "address")
    PHONE = (By.NAME, "phone")
    EMAIL = (By.NAME, "email")
    #ADDPERSON = (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[2]/form/label/span")
    BTN_TO_PAY = (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[2]/form/div[5]/button")

class PaymentPageLocators():
    SUM_POLIS = (By.CSS_SELECTOR, ' tui-money > span:nth-child(2)')

class EmptyLocators():
    EMPTY_PARS = [
    (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[2]/form/div[1]/div[1]/div[1]/div[3]"),
    (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[2]/form/div[1]/div[1]/div[2]/div"),
    (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div[1]/div"),
    (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div[2]/div"),
    (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[2]/form/div[1]/div[3]/div[2]"),
    (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[2]/form/div[1]/div[4]/div[1]/div"),
    (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div[1]/div/div/div[2]/form/div[1]/div[4]/div[2]/div[2]")
    ]
