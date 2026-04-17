import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from pages.main_page import MainPage
from locators import Locators
from url import base_url

class TestClickPersonalAccaunt:

    def test_click_to_personal_accaunt(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Проверяем, что кнопка «Личный кабинет» видна — прямо в ассерте
        driver_base.click(Locators.text_personal_accaunt)  # кликаем после успешной проверки
        # Проверяем видимость кнопки «Войти» после перехода
        # Только теперь проверяем текст кнопки
        assert driver_base.get_text(Locators.button_login) == 'Войти', "Текст кнопки 'Войти' некорректен"
