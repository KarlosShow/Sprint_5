import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import time
from pages.main_page import MainPage
from pages.base_page import BasePage
from locators import Locators
import config
from url import base_url
import pytest

class TestNavigationInConstructor:
    
    @pytest.mark.parametrize('tab_locator', config.tabs)
    def test_tab_activation_class(self, driver, tab_locator):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Проверяем, что конструктор загружен
        assert driver_base.element_visible(Locators.text_get_burger), "Элемент 'Соберите бургер' не виден — конструктор не загружен"
        # Кликаем на таб
        driver_base.click(tab_locator)
        # Получаем локатор для активного класса этого таба
        active_class_locator = config.tab_to_active_class[tab_locator]
        # Проверяем, появился ли класс активности
        assert driver_base.has_class(active_class_locator), f"Класс активного таба не появился для {tab_locator}"
    
    def test_navigation_in_constructor_by_section_rolls(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.find(Locators.text_get_burger)
        driver_base.click(Locators.text_sauces)
        driver_base.click(Locators.text_rools)
        assert driver_base.element_visible(Locators.rolls_active), "Таб 'Булки' не стал активным"

    def test_navigation_in_constructor_by_section_sauces(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.find(Locators.text_get_burger)
        driver_base.click(Locators.text_sauces)
        assert driver_base.element_visible(Locators.sauces_active), "Раздел 'Соусы' не выбран"

    def test_navigation_in_constructor_by_section_fillings(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.find(Locators.text_get_burger)
        driver_base.click(Locators.text_fillings)
        assert driver_base.element_visible(Locators.fillings_active), "Раздел 'Начинки' не выбран"
    
