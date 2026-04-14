import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from main import MainPage
from locators import Locators
from url import base_url

class TestMoveFromAccauntToConstructor:

    def test_move_from_personal_accaunt_to_constructor_by_text_consnructor(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.find(Locators.text_personal_accaunt)
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.text_constructor)
        driver_base.click(Locators.text_constructor)
        driver_base.find(Locators.text_get_burger)
        assert driver_base.get_text(Locators.text_get_burger) == 'Соберите бургер'

    def test_move_from_personal_accaunt_to_constructor_by_logotip(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.find(Locators.text_personal_accaunt)
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.logotip)
        driver_base.click(Locators.logotip)
        driver_base.find(Locators.text_get_burger)
        assert driver_base.get_text(Locators.text_get_burger) == 'Соберите бургер'
