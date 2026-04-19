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
        
    @pytest.mark.parametrize('tab_locator', [config.tabs[1], config.tabs[2]])  # исключаем первый таб (Булки)
    def test_tab_activation_class(self, driver, tab_locator):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Проверяем загрузку конструктора
        driver_base.element_visible(Locators.text_get_burger)
        driver_base.click(tab_locator)
        active_class_locator = config.tab_to_active_class[tab_locator]
        # проверяем, что элемент активного таба найден
        assert driver_base.find(active_class_locator), f"Таб {tab_locator} не стал активным"

    # Отдельный тест для «Булок»
    def test_rolls_tab_reactivation(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Сначала кликаем на другой таб (например, «Соусы»)
        driver_base.click(config.tabs[1])  # Предполагаем, что это «Соусы»
        # Затем кликаем обратно на «Булки»
        driver_base.click(Locators.text_rools)
        # проверяем, что «Булки» стали активными
        assert driver_base.find(config.tab_to_active_class[Locators.text_rools]), "Таб 'Булки' не стал активным"

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
    
