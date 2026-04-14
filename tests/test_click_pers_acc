import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from main import MainPage
from locators import Locators
from url import base_url

class TestClickPersonalAccaunt:

    def test_click_to_personal_accaunt(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.find(Locators.text_personal_accaunt)
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.button_login)
        assert driver_base.get_text(Locators.button_login) == 'Войти'