import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from main import MainPage
from locators import Locators
from url import base_url
from good_acc import *

class TestEnterFromAccaunt:
    
    def test_enter_by_button_enter_in_accaunt(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.click(Locators.button_login_account)
        driver_base.type(Locators.email_input, r_email)
        driver_base.type(Locators.password_input, r_pass)
        driver_base.click(Locators.button_login)
        driver_base.find(Locators.text_personal_accaunt)
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.username_input)
        assert driver_base.get_attribute_value(Locators.username_input, "value") == r_name

    def test_enter_by_button_in_personal_accaunt(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.button_login)
        driver_base.type(Locators.email_input, r_email)
        driver_base.type(Locators.password_input, r_pass)
        driver_base.click(Locators.button_login)
        driver_base.find(Locators.text_personal_accaunt)
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.username_input)
        assert driver_base.get_attribute_value(Locators.username_input, "value") == r_name
    
    def test_enter_by_button_in_registration_form(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.find(Locators.text_personal_accaunt)
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.text_checkin)
        driver_base.click(Locators.text_checkin)
        driver_base.find(Locators.text_login)
        driver_base.click(Locators.text_login)
        driver_base.find(Locators.button_login)
        driver_base.type(Locators.email_input, r_email)
        driver_base.type(Locators.password_input, r_pass)
        driver_base.click(Locators.button_login)
        driver_base.find(Locators.text_personal_accaunt)
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.username_input)
        assert driver_base.get_attribute_value(Locators.username_input, "value") == r_name

    def test_enter_by_button_of_recovery_password(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.find(Locators.text_personal_accaunt)
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.text_recovery_pass)
        driver_base.click(Locators.text_recovery_pass)
        driver_base.find(Locators.text_login)
        driver_base.click(Locators.text_login)
        driver_base.find(Locators.button_login)
        driver_base.type(Locators.email_input, r_email)
        driver_base.type(Locators.password_input, r_pass)
        driver_base.click(Locators.button_login)
        driver_base.find(Locators.text_personal_accaunt)
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.username_input)
        assert driver_base.get_attribute_value(Locators.username_input, "value") == r_name
