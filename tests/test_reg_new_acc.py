import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from pages.main_page import MainPage
from locators import Locators
from url import *
from good_acc import *

class TestRegistration:

    def test_successful_registration(self, driver, rdata_for_good_reg):
        driver_base = MainPage(driver)
        driver_base.open(reg_url)
        new_name, new_email, new_password = rdata_for_good_reg
        # вводим данные
        driver_base.type(Locators.username_input, new_name)
        driver_base.type(Locators.email_input, new_email)
        driver_base.type(Locators.password_input, new_password)
        driver_base.click(Locators.button_checkinn)
        # Проверяем, что кнопка «Войти» появилась
        assert driver_base.element_visible(Locators.button_login), "Кнопка 'Войти' не видна после регистрации"
        # Выполняем вход
        driver_base.type(Locators.email_input, new_email)
        driver_base.type(Locators.password_input, new_password)
        driver_base.click(Locators.button_login)
        # Переходим в личный кабинет
        assert driver_base.element_visible(Locators.text_personal_accaunt), "Кнопка 'Личный кабинет' не видна на главной странице"
        driver_base.click(Locators.text_personal_accaunt)

        # проверяем результат регистрации
        assert driver_base.get_attribute_value(Locators.displayed_username, "value") == new_name
        # assert driver_base.get_text(Locators.displayed_username) == new_name, "Имя пользователя не отображается в профиле"

    def test_invalid_password_by_registration(self, driver, rdata_for_badpass_reg):
        driver_base = MainPage(driver)
        driver_base.open(reg_url)
        new_name, new_email, new_password = rdata_for_badpass_reg
        driver_base.type(Locators.username_input, new_name)
        driver_base.type(Locators.email_input, new_email)
        driver_base.type(Locators.password_input, new_password)
        driver_base.click(Locators.button_checkinn)
        assert driver_base.get_text(Locators.invalid_pass_reg) == "Некорректный пароль"
        