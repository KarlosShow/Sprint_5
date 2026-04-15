import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from main import MainPage
from locators import Locators
from url import base_url
from good_acc import *

class TestClickExit:

    def test_exit_from_accaunt(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Логинимся
        driver_base.click(Locators.button_login_account)
        driver_base.type(Locators.email_input, r_email)
        driver_base.type(Locators.password_input, r_pass)
        driver_base.click(Locators.button_login)
        # Проверяем, что кнопка «Личный кабинет» видна — прямо в ассерте
        assert driver_base.element_visible(Locators.text_personal_accaunt), "Кнопка 'Личный кабинет' не видна после логина"
        driver_base.click(Locators.text_personal_accaunt)
        # Проверяем, что поле имени пользователя видно — тоже в ассерте
        assert driver_base.element_visible(Locators.username_input), "Поле имени пользователя не видно в ЛК"
        driver_base.find(Locators.username_input)  # поиск для взаимодействия
        # Выходим из аккаунта
        driver_base.click(Locators.button_logout)
        # Проверяем результат выхода — поле email должно быть пустым
        assert driver_base.get_attribute_value(Locators.email_input, "value") == "", "Поле email не очистилось после выход
        