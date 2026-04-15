import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from main import MainPage
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
        driver_base.type(Locators.email_input, r_email)
        driver_base.type(Locators.password_input, r_pass)
        driver_base.click(Locators.button_login)
        # 3. Проверяем видимость кнопки «Личный кабинет» прямо в ассерте
        assert driver_base.element_visible(Locators.text_personal_accaunt), "Кнопка 'Личный кабинет' не видна после логина"
        driver_base.click(Locators.text_personal_accaunt)  # кликаем после успешной проверки

        # Проверяем видимость поля имени пользователя
        assert driver_base.element_visible(Locators.username_input), "Поле имени пользователя не видно в ЛК"
        driver_base.find(Locators.username_input)  # поиск для взаимодействия

        # Проверяем, что имя пользователя отображается корректно
        assert driver_base.get_attribute_value(Locators.username_input, "value") == r_name, "Имя пользователя не соответствует ожидаемому"

    def test_enter_by_button_in_personal_accaunt(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Проверяем видимость кнопки «Личный кабинет»
        assert driver_base.element_visible(Locators.text_personal_accaunt), "Кнопка 'Личный кабинет' не видна на главной странице"
        driver_base.click(Locators.text_personal_accaunt)  # кликаем после успешной проверки

        # Проверяем видимость кнопки «Войти»
        assert driver_base.element_visible(Locators.button_login), "Кнопка 'Войти' не видна после перехода в ЛК"

        # Выполняем вход
        driver_base.type(Locators.email_input, r_email)
        driver_base.type(Locators.password_input, r_pass)
        driver_base.click(Locators.button_login)

        # Переходим в личный кабинет и проверяем элементы
        assert driver_base.element_visible(Locators.text_personal_accaunt), "Кнопка 'Личный кабинет' снова не видна"
        driver_base.click(Locators.text_personal_accaunt)
        assert driver_base.element_visible(Locators.username_input), "Поле имени пользователя не видно"
        driver_base.find(Locators.username_input)  # поиск для взаимодействия

        # Проверяем имя пользователя
        assert driver_base.get_attribute_value(Locators.username_input, "value") == r_name, "Имя пользователя не соответствует ожидаемому"
 
    
    def test_enter_by_button_in_registration_form(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Переходим к форме регистрации
        assert driver_base.element_visible(Locators.text_personal_accaunt), "Кнопка 'Личный кабинет' не видна на главной странице"
        driver_base.click(Locators.text_personal_accaunt)  # кликаем после успешной проверки
        assert driver_base.element_visible(Locators.text_checkin), "Кнопка регистрации не видна"
        driver_base.click(Locators.text_checkin)  # переход к форме 

    def test_enter_by_button_of_recovery_password(self, driver):
        driver_base = MainPage(driver)
        driver_base.open(base_url)
        # Переходим к восстановлению пароля
        assert driver_base.element_visible(Locators.text_personal_accaunt), "Кнопка 'Личный кабинет' не видна на главной странице"
        driver_base.click(Locators.text_personal_accaunt)  # кликаем после успешной проверки
        assert driver_base.element_visible(Locators.text_recovery_pass), "Кнопка восстановления пароля не видна"
        driver_base.click(Locators.text_recovery_pass)  # переход к форме восстановления

        # Возвращаемся к форме входа
        assert driver_base.element_visible(Locators.text_login), "Кнопка входа не видна после перехода к восстановлению"
        driver_base.click(Locators.text_login)  # возврат к форме входа

        # Выполняем вход
        assert driver_base.element_visible(Locators.button_login), "Кнопка 'Войти' не видна в форме входа"
        driver_base.type(Locators.email_input, r_email)
        driver_base.type(Locators.password_input, r_pass)
        driver_base.click(Locators.button_login)

        # Переходим в личный кабинет и проверяем элементы
        assert driver_base.element_visible(Locators.text_personal_accaunt), "Кнопка 'Личный кабинет' снова не видна"
        driver_base.click(Locators.text_personal_accaunt)
        assert driver_base.element_visible(Locators.username_input), "Поле имени пользователя не видно"
        driver_base.find(Locators.username_input)  # поиск для взаимодействия

        # Проверяем имя пользователя
        assert driver_base.get_attribute_value(Locators.username_input, "value") == r_name, "Имя пользователя не соответствует ожидаемому"
