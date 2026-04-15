import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
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
        # Убеждаемся, что открыты страницы конструктора
        assert driver_base.element_visible(Locators.text_get_burger), "Конструктор не загружен — элемент 'Соберите бургер' не виден"

        # Переходим к разделу соусов, чтобы попасть в конструктор
        driver_base.click(Locators.text_sauces)

        # Переходим в раздел булочек
        driver_base.click(Locators.text_rools)

        # Проверяем, что раздел булочек выбран
        assert driver_base.element_visible(Locators.rolls_active), "Раздел 'Булочки' не выбран"

    def test_navigation_in_constructor_by_section_sauces(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Убеждаемся, что открыты страницы конструктора
        assert driver_base.element_visible(Locators.text_get_burger), "Конструктор не загружен — элемент 'Соберите бургер' не виден"

        # Переходим к разделу соусов
        driver_base.click(Locators.text_sauces)

        # Проверяем, что раздел соусов выбран
        assert driver_base.element_visible(Locators.sauces_active), "Раздел 'Соусы' не выбран"

    def test_navigation_in_constructor_by_section_fillings(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Убеждаемся, что открыты страницы конструктора
        assert driver_base.element_visible(Locators.text_get_burger), "Конструктор не загружен — элемент 'Соберите бургер' не виден"

        # Переходим к разделу начинок
        driver_base.click(Locators.text_fillings)

        # Проверяем, что раздел начинок выбран
        assert driver_base.element_visible(Locators.fillings_active), "Раздел 'Начинки' не выбран"
