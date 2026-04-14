Stella Burger UI tests

Все тесты расположены в папке tests:
test_click_pers_acc.py кнопка личный аккаунт
test_enter_anywhere.py кнопка войти из разных мест сайта
test_exit_acc.py кнопка выхода из аккаунта
test_move_acc_from_constructor.py переходы в контруктор из аккаунта
test_navigation_take_burger.py переходы булки соусы начинки
test_reg_new_acc.py регистрация

доп файлы:
conftest.py для фикстур
url.py содержит url
good_acc.py мой рабочий аккаунт
locators.py все необходимые для тестов локаторы
main.py файл содержит базовые методы

Запускаем тесты командой pytest -v в корне проекта
Мне нравится что получилось 14.04.2026 14:05

platform win32 -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\Сергей\AppData\Local\Programs\Python\Py
thon314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Сергей\sprint_5k
plugins: cov-7.0.0
collected 16 items

tests/test_click_pers_acc.py::TestClickPersonalAccaunt::test_click_to_personal_accaunt PASSED           [  6%]
tests/test_enter_anywhere.py::TestEnterFromAccaunt::test_enter_by_button_enter_in_accaunt PASSED        [ 12%]
tests/test_enter_anywhere.py::TestEnterFromAccaunt::test_enter_by_button_in_personal_accaunt PASSED     [ 18%]
tests/test_enter_anywhere.py::TestEnterFromAccaunt::test_enter_by_button_in_registration_form PASSED    [ 25%]
tests/test_enter_anywhere.py::TestEnterFromAccaunt::test_enter_by_button_of_recovery_password PASSED    [ 31%]
tests/test_exit_acc.py::TestClickExit::test_exit_from_accaunt PASSED                                    [ 37%]
tests/test_move_acc_from_constructor.py::TestMoveFromAccauntToConstructor::test_move_from_personal_accaunt_to_c
onstructor_by_text_consnructor PASSED [ 43%]
tests/test_move_acc_from_constructor.py::TestMoveFromAccauntToConstructor::test_move_from_personal_accaunt_to_c
onstructor_by_logotip PASSED [ 50%]
tests/test_navigation_take_burger.py::TestNavigationInConstructor::test_navigation_in_constructor_by_elements[i
mage0] PASSED [ 56%]
tests/test_navigation_take_burger.py::TestNavigationInConstructor::test_navigation_in_constructor_by_elements[i
mage1] PASSED [ 62%]
tests/test_navigation_take_burger.py::TestNavigationInConstructor::test_navigation_in_constructor_by_elements[i
mage2] PASSED [ 68%]
tests/test_navigation_take_burger.py::TestNavigationInConstructor::test_navigation_in_constructor_by_section_ro
lls PASSED [ 75%]
tests/test_navigation_take_burger.py::TestNavigationInConstructor::test_navigation_in_constructor_by_section_sa
uces PASSED [ 81%]
tests/test_navigation_take_burger.py::TestNavigationInConstructor::test_navigation_in_constructor_by_section_fi
llings PASSED [ 87%]
tests/test_reg_new_acc.py::TestRegistration::test_successful_registration PASSED                        [ 93%]
tests/test_reg_new_acc.py::TestRegistration::test_invalid_password_by_registration PASSED               [100%]

======================================= 16 passed in 124.79s (0:02:04) =======================================
