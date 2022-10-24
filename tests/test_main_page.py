from .pages.main_page import MainPage
from allure_commons.types import AttachmentType
import allure, pytest, time


@allure.feature("Tests for absolute")
@allure.story("Расчет и переход к оплате полиса")
@pytest.mark.calc_polis
@pytest.mark.parametrize(
    "strah_sum, client_fio, client_birth, client_p_n, client_p_d, client_addr, client_phone, client_mail, test_flag",
    [
        (
            "100 000",
            "Иванов Иван Иванович",
            "12.04.1999",
            "5004 678901",
            "12.05.2016",
            "г Москва, ул Академика Королева, влд 2А ",
            "9034567788",
            "mail7531@gmail.com",
            "p",
        ),
        (
            "500 000",
            "Петрова Анна",
            "05.10.1990",
            "5009 778900",
            "31.01.2010",
            "г Новосибирск, ул 1905 года, д 20 ",
            "9134569988",
            "petro7431@gmail.com",
            "p",
        ),
        (
            "",
            "Сидоров Сидор Сидорович",
            "05.10.1990",
            "5009 778900",
            "31.01.2010",
            "г Краснодар, ул Освободителей Краснодара, д 3 ",
            "9034567788",
            "mail7531@gmail.com",
            "p",
        ),
        (
            "100 000",
            "",
            "05.10.1990",
            "5009 778900",
            "31.01.2010",
            "г Краснодар, ул Освободителей Краснодара, д 3 ",
            "9034567788",
            "mail7531@gmail.com",
            "n",
        ),
        (
            "",
            "Иванов Иван Иванович",
            "",
            "5004 678901",
            "12.05.2016",
            "г Москва, ул Академика Королева, влд 2А ",
            "9034567788",
            "mail7531@gmail.com",
            "n",
        ),
        (
            "100 000",
            "Иванов Иван Иванович",
            "12.04.1999",
            "",
            "12.05.2016",
            "г Москва, ул Академика Королева, влд 2А ",
            "9034567788",
            "mail7531@gmail.com",
            "n",
        ),
        (
            "500 000",
            "Иванов Иван Иванович",
            "12.04.1999",
            "5004 678901",
            "",
            "г Москва, ул Академика Королева, влд 2А ",
            "9034567788",
            "mail7531@gmail.com",
            "n",
        ),
        (
            "",
            "Иванов Иван Иванович",
            "12.04.1999",
            "5004 678901",
            "12.05.2016",
            "",
            "9034567788",
            "mail7531@gmail.com",
            "n",
        ),
        (
            "100 000",
            "Иванов Иван Иванович",
            "12.04.1999",
            "5004 678901",
            "12.05.2016",
            "г Москва, ул Академика Королева, влд 2А ",
            "",
            "mail7531@gmail.com",
            "n",
        ),
        (
            "500 000",
            "Иванов Иван Иванович",
            "12.04.1999",
            "5004 678901",
            "12.05.2016",
            "г Москва, ул Академика Королева, влд 2А ",
            "9034567788",
            "",
            "n",
        ),
        ("", "", "12.04.1999", "", "12.05.2016", "", "9034567788", "", "n"),
        (
            "100 000",
            "Иванов Иван Иванович",
            "",
            "5004 678901",
            "",
            "г Москва, ул Академика Королева, влд 2А ",
            "",
            "mail7531@gmail.com",
            "n",
        ),
    ],
)
class TestCalcPolis:
    def test_calc_polis(
        self,
        browser,
        strah_sum,
        client_fio,
        client_birth,
        client_p_n,
        client_p_d,
        client_addr,
        client_phone,
        client_mail,
        test_flag,
    ):
        link = "https://old.absolutins.ru/kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/zashchita-ot-virusa/"
        page = MainPage(browser, link)
        with allure.step("Переходим на страницу покупки полиса"):
            page.open()
        with allure.step("Выполняем предвариетельный расчет полиса"):
            str_sum = strah_sum
            page.predcalculate_polis(str_sum)
        with allure.step(
            "Проверим, что сумма госпитализации и стоимость полиса рассчитаны верно"
        ):
            allure.attach(
                browser.get_screenshot_as_png(),
                name="Форма предвариетльного расчета",
                attachment_type=AttachmentType.PNG,
            )
            sum_polis = page.should_be_sums(str_sum)
        with allure.step("Переходим на страницу ввода данных"):
            page.go_to_filling()
        with allure.step("Вводим необходимые данные"):
            fio = client_fio
            birth_date = client_birth
            passport_num = client_p_n
            passport_date = client_p_d
            address = client_addr
            phone = client_phone
            email = client_mail
            # addperson = "ON"
            page.fill_form(
                fio, birth_date, passport_num, passport_date, address, phone, email
            )
            allure.attach(
                browser.get_screenshot_as_png(),
                name="Страница ввода данных",
                attachment_type=AttachmentType.PNG,
            )
        with allure.step("Переходим в кабинет оплаты"):
            page.go_to_pay()
        time.sleep(20)
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Страница оплаты",
            attachment_type=AttachmentType.PNG,
        )
        if test_flag == "p":
            with allure.step(
                "Проверим, что переход на страницу оплаты осуществлен и сумма рассчитана верно"
            ):
                page.should_be_payment_page(sum_polis)
        else:
            with allure.step(
                "Проверим, что переход на страницу оплаты не был выполнен"
            ):
                page.should_not_be_payment_url()
                empty_param = [
                    client_fio,
                    client_birth,
                    client_p_n,
                    client_p_d,
                    client_addr,
                    client_phone,
                    client_mail,
                ]
                for i in range(len(empty_param)):
                    if empty_param[i] == "":
                        with allure.step(
                            "Проверим, что появляется верное сообщение о пустом поле"
                        ):
                            page.should_empty_message(i)
