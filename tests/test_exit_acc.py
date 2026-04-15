import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from main import MainPage
from locators import Locators
from url import base_url
from good_acc import *

class TestClickExit:

    def test_exit_from_accaunt(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.click(Locators.button_login_account)
        driver_base.type(Locators.email_input, r_email)
        driver_base.type(Locators.password_input, r_pass)
        driver_base.click(Locators.button_login)
        driver_base.find(Locators.text_personal_accaunt)
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.username_input)
        driver_base.click(Locators.button_logout)
        assert driver_base.get_attribute_value(Locators.email_input, "value") == ""
        