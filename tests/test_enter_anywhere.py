import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from pages.main_page import MainPage
from locators import Locators
from url import base_url
from good_acc import *

class TestEnterFromAccaunt:
    
    def test_enter_by_button_enter_in_accaunt(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # кликаем на кнопку войти в аккаунт
        driver_base.click(Locators.button_login_account)
        # Вводим данные и логинимся
        driver_base.type(Locators.email_input, good_email)
        driver_base.type(Locators.password_input, good_pass)
        driver_base.click(Locators.button_login)
        # 3. Проверяем видимость кнопки «Личный кабинет» прямо в ассерте
        driver_base.click(Locators.text_personal_accaunt)  # кликаем после успешной проверки

        # Проверяем видимость поля имени пользователя
        driver_base.find(Locators.username_input)  # поиск для взаимодействия

        # Проверяем, что имя пользователя отображается корректно
        assert driver_base.get_attribute_value(Locators.username_input, "value") == good_name, "Имя пользователя не соответствует ожидаемому"

    def test_enter_by_button_in_personal_accaunt(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Проверяем видимость кнопки «Личный кабинет»
        driver_base.click(Locators.text_personal_accaunt)  # кликаем после успешной проверки

        # Проверяем видимость кнопки «Войти»

        # Выполняем вход
        driver_base.type(Locators.email_input, good_email)
        driver_base.type(Locators.password_input, good_pass)
        driver_base.click(Locators.button_login)

        # Переходим в личный кабинет и проверяем элементы
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.username_input)  # поиск для взаимодействия

        # Проверяем имя пользователя
        assert driver_base.get_attribute_value(Locators.username_input, "value") == good_name, "Имя пользователя не соответствует ожидаемому"
 
    
    def test_enter_by_button_in_registration_form(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Переходим к форме регистрации
        driver_base.click(Locators.text_personal_accaunt)  # кликаем после успешной проверки
        assert driver_base.element_visible(Locators.text_checkin), "Кнопка регистрации не видна"
        driver_base.click(Locators.text_checkin)  # переход к форме 

    def test_enter_by_button_of_recovery_password(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Переходим к восстановлению пароля
        driver_base.click(Locators.text_personal_accaunt)  # кликаем после успешной проверки
        driver_base.click(Locators.text_recovery_pass)  # переход к форме восстановления

        # Возвращаемся к форме входа
        driver_base.click(Locators.text_login)  # возврат к форме входа

        # Выполняем вход
        driver_base.type(Locators.email_input, good_email)
        driver_base.type(Locators.password_input, good_pass)
        driver_base.click(Locators.button_login)

        # Переходим в личный кабинет и проверяем элементы
        driver_base.click(Locators.text_personal_accaunt)
        driver_base.find(Locators.username_input)  # поиск для взаимодействия

        # Проверяем имя пользователя
        assert driver_base.get_attribute_value(Locators.username_input, "value") == good_name, "Имя пользователя не соответствует ожидаемому"
