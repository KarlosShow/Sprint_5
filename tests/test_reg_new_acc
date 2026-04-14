import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from main import MainPage
from locators import Locators
from url import *
from good_acc import *

class TestRegistration:

    def test_successful_registration(self, driver, create_data_for_succes_reg):
        driver_base = MainPage(driver)
        driver_base.open(reg_url)
        new_name, new_email, new_password = create_data_for_succes_reg
        driver_base.type(Locators.username_input, new_name)
        driver_base.type(Locators.email_input, new_email)
        driver_base.type(Locators.password_input, new_password)
        driver_base.click(Locators.button_checkinn)
        driver_base.find(Locators.button_login)
        driver_base.type(Locators.email_input, new_email)
        driver_base.type(Locators.password_input, new_password)
        driver_base.click(Locators.button_login)
        driver_base.find(Locators.text_personal_accaunt)
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.username_input)
        assert driver_base.get_attribute_value(Locators.username_input, "value") == new_name

    def test_invalid_password_by_registration(self, driver, create_data_for_invalid_reg_by_password):
        driver_base = MainPage(driver)
        driver_base.open(reg_url)
        new_name, new_email, new_password = create_data_for_invalid_reg_by_password
        driver_base.type(Locators.username_input, new_name)
        driver_base.type(Locators.email_input, new_email)
        driver_base.type(Locators.password_input, new_password)
        driver_base.click(Locators.button_checkinn)
        assert driver_base.get_text(Locators.invalid_pass_reg) == "Некорректный пароль"