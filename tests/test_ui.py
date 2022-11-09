import pytest

from base.base_logic import BaseLogic


@pytest.mark.usefixtures("setup")
class TestUi:

    def test_case1(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.input_in_fields_authorization_and_submit("+3754%№;:?*", "skalskdncnc")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold").get_attribute(
            "textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case2(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.input_in_fields_authorization_and_submit("+79000000000", "skalskdncnc")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold").get_attribute(
            "textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case3(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.input_in_fields_authorization_and_submit("+79000000000", ":№;%?*DHJ")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold").get_attribute(
            "textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case4(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.input_in_fields_authorization_and_submit("", "")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold").get_attribute(
            "textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case5(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.input_in_fields_authorization_and_submit("+79000000000", "")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold").get_attribute(
            "textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case6(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.are_present("class_name", "rt-tab--small")[1].click()
        test_object.input_in_fields_authorization_and_submit("324gsdus@gmail.com", "sudvybusdvuyusv")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold") \
            .get_attribute("textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case7(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.are_present("class_name", "rt-tab--small")[1].click()
        test_object.input_in_fields_authorization_and_submit("", "")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold") \
            .get_attribute("textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case8(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.are_present("class_name", "rt-tab--small")[1].click()
        test_object.input_in_fields_authorization_and_submit("324gsdus@gmail.com", "")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold") \
            .get_attribute("textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case9(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.are_present("class_name", "rt-tab--small")[1].click()
        test_object.input_in_fields_authorization_and_submit("jksv#$^%^&*", "$&&&*(")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold") \
            .get_attribute("textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case10(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.are_present("class_name", "rt-tab--small")[2].click()
        test_object.input_in_fields_authorization_and_submit("", "")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold") \
            .get_attribute("textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case11(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.are_present("class_name", "rt-tab--small")[2].click()
        test_object.input_in_fields_authorization_and_submit("$&&&*(", "$&&&*(")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold") \
            .get_attribute("textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case12(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.are_present("class_name", "rt-tab--small")[2].click()
        test_object.input_in_fields_authorization_and_submit("Login2792472", "")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold") \
            .get_attribute("textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case13(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.are_present("class_name", "rt-tab--small")[2].click()
        test_object.input_in_fields_authorization_and_submit("Login2792472", "Bisac456823")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold") \
            .get_attribute("textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case14(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.are_present("class_name", "rt-tab--small")[3].click()
        test_object.input_in_fields_authorization_and_submit("", "")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold") \
            .get_attribute("textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case15(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.are_present("class_name", "rt-tab--small")[3].click()
        test_object.input_in_fields_authorization_and_submit("23872835832", "")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold") \
            .get_attribute("textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case16(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.are_present("class_name", "rt-tab--small")[3].click()
        test_object.input_in_fields_authorization_and_submit("23872835832", "gvdsvjs76352736")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold") \
            .get_attribute("textContent")
        assert error_text.lower() == " неверный логин или пароль"

    def test_case17(self):
        test_object: BaseLogic = BaseLogic(self.driver, 10, 0.1)
        test_object.are_present("class_name", "rt-tab--small")[3].click()
        test_object.input_in_fields_authorization_and_submit("%:?(*:?:%", ";%::?*?:%")
        error_text: str = test_object.is_present("class_name", "login-form-container__error--bold") \
            .get_attribute("textContent")
        assert error_text.lower() == " неверный логин или пароль"
