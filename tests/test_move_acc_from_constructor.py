import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from pages.main_page import MainPage
from locators import Locators
from url import base_url

class TestMoveFromAccauntToConstructor:

    def test_move_from_personal_accaunt_to_constructor_by_text_consnructor(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Переходим в личный кабинет
        driver_base.click(Locators.text_personal_accaunt)
        # Переходим к конструктору
        driver_base.click(Locators.text_constructor)
        # Проверяем, что мы попали в конструктор
        assert driver_base.get_text(Locators.text_get_burger) == 'Соберите бургер', "Текст элемента 'Соберите бургер' некорректен"

    def test_move_from_personal_accaunt_to_constructor_by_logotip(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Переходим в личный кабинет
        driver_base.click(Locators.text_personal_accaunt)
        # Кликаем по логотипу
        driver_base.click(Locators.logotip)
        # Проверяем, что мы попали в конструктор
        assert driver_base.get_text(Locators.text_get_burger) == 'Соберите бургер', "Текст элемента 'Соберите бургер' некорректен"
