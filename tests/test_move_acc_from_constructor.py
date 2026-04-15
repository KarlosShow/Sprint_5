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
        # Переходим в личный кабинет
        assert driver_base.element_visible(Locators.text_personal_accaunt), "Кнопка 'Личный кабинет' не видна на главной странице"
        driver_base.click(Locators.text_personal_accaunt)

        # Переходим к конструктору
        assert driver_base.element_visible(Locators.text_constructor), "Кнопка конструктора не видна в личном кабинете"
        driver_base.click(Locators.text_constructor)

        # Проверяем, что мы попали в конструктор
        assert driver_base.element_visible(Locators.text_get_burger), "Элемент 'Соберите бургер' не виден после перехода в конструктор"
        assert driver_base.get_text(Locators.text_get_burger) == 'Соберите бургер', "Текст элемента 'Соберите бургер' некорректен"

    def test_move_from_personal_accaunt_to_constructor_by_logotip(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Переходим в личный кабинет
        assert driver_base.element_visible(Locators.text_personal_accaunt), "Кнопка 'Личный кабинет' не видна на главной странице"
        driver_base.click(Locators.text_personal_accaunt)

        # Кликаем по логотипу
        assert driver_base.element_visible(Locators.logotip), "Логотип не виден в личном кабинете"
        driver_base.click(Locators.logotip)

        # Проверяем, что мы попали в конструктор
        assert driver_base.element_visible(Locators.text_get_burger), "Элемент 'Соберите бургер' не виден после перехода в конструктор"
        assert driver_base.get_text(Locators.text_get_burger) == 'Соберите бургер', "Текст элемента 'Соберите бургер' некорректен"
