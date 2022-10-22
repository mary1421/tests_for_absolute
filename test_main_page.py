import pytest, time
from .pages.main_page import MainPage

@pytest.mark.calc_polis
@pytest.mark.parametrize(
    "client_fio, client_birth, client_p_n, client_p_d, client_addr, client_phone, client_mail, test_flag",
    [
        ("Иванов Иван Иванович", '12.04.1999', '5004 678901', '12.05.2016',
        'г Москва, ул Академика Королева, влд 2А ', '9034567788', 'mail7531@gmail.com', 'p'),
        #("", '05.10.1990', '5004 678901', '12.05.2016',
        #'г Москва, ул Академика Королева, влд 2А ','9134569988', 'petro7431@gmail.com', 'n'),
        #("Иванов Иван Иванович", '', '5004 678901', '12.05.2016',
        # 'г Москва, ул Академика Королева, влд 2А ', '9034567788', 'mail7531@gmail.com', 'n'),
        #("Иванов Иван Иванович", '12.04.1999', '', '12.05.2016',
        #'г Москва, ул Академика Королева, влд 2А ', '9034567788', 'mail7531@gmail.com', 'n'),
        #("Иванов Иван Иванович", '12.04.1999', '5004 678901', '',
        #'г Москва, ул Академика Королева, влд 2А ', '9034567788', 'mail7531@gmail.com', 'n'),
        #("Иванов Иван Иванович", '12.04.1999', '5004 678901', '12.05.2016',
        #'', '9034567788', 'mail7531@gmail.com', 'n'),
        #("Иванов Иван Иванович", '12.04.1999', '5004 678901', '12.05.2016',
        #'г Москва, ул Академика Королева, влд 2А ', '', 'mail7531@gmail.com', 'n'),
        #("Иванов Иван Иванович", '12.04.1999', '5004 678901', '12.05.2016',
        #'г Москва, ул Академика Королева, влд 2А ', '9034567788', '', 'n')
    ]
)
class TestCalcPolis():
    def test_calc_polis(self, browser, client_fio, client_birth, client_p_n, client_p_d, client_addr, \
                                         client_phone, client_mail, test_flag):
        link = "https://old.absolutins.ru/kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/zashchita-ot-virusa/"
        page = MainPage(browser, link)
        page.open()
        sum_polis = page.predcalculate_polis()
        fio = client_fio
        birth_date = client_birth
        passport_num = client_p_n
        passport_date = client_p_d
        address = client_addr
        phone = client_phone
        email = client_mail
        #addperson = "ON"
        page.fill_form(fio, birth_date, passport_num, passport_date, address, phone, email)
        page.go_to_pay()
        time.sleep(20)
        if test_flag == 'p':
            page.should_be_payment_page(sum_polis)
        else:
            page.should_not_be_payment_page()
            empty_param = [client_fio, client_birth, client_p_n, client_p_d, client_addr, \
                                         client_phone, client_mail]
            for i in range(len(empty_param)):
                if empty_param[i] == '':
                 page.should_empty_message(i)

