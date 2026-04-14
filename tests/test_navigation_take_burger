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
        driver_base.find(Locators.text_get_burger)
        element_img = driver_base.element_visible(image)
        assert element_img.is_displayed()

    def test_navigation_in_constructor_by_section_rolls(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.find(Locators.text_get_burger)
        driver_base.click(Locators.text_sauces)
        driver_base.click(Locators.text_rools)
        active_element = driver_base.element_visible(Locators.rolls_active)
        assert active_element is not None, "Раздел не выбран"

    def test_navigation_in_constructor_by_section_sauces(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.find(Locators.text_get_burger)
        driver_base.click(Locators.text_sauces)
        active_element = driver_base.element_visible(Locators.sauces_active)
        assert active_element is not None, "Раздел не выбран"

    def test_navigation_in_constructor_by_section_fillings(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        driver_base.find(Locators.text_get_burger)
        driver_base.click(Locators.text_fillings)
        active_element = driver_base.element_visible(Locators.fillings_active)
        assert active_element is not None, "Раздел не выбран"
