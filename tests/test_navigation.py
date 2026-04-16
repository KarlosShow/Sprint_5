import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import time
from main import MainPage
from locators import Locators
from url import base_url
import pytest

class TestNavigationInConstructor:
    images = [Locators.img_1rools, Locators.img_1fillings, Locators.img_1fillings]

    @pytest.mark.parametrize('image', images)
    def test_navigation_in_constructor_by_elements(self, driver, image):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Проверяем, что мы находимся в конструкторе
        assert driver_base.element_visible(Locators.text_get_burger), "Элемент 'Соберите бургер' не виден — конструктор не загружен"
        # Проверяем видимость нужного изображения
        assert driver_base.element_visible(image), f"Изображение {image} не видно в конструкторе"
    
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
    
