from selenium.webdriver.common.by import By

class Locators:
    button_personal_accaunt = (By.XPATH, "//a[@class ='AppHeader_header__linkText__3q_va ml-2']") #кнопка личный кабинет
    t_button_checkin = (By.XPATH, "//a[@class = 'Auth_link__1fOlj']") # текст кнопка зарегестрироваться
    username_input = (By.XPATH, ".//label[text()='Имя']/..//input") # поле имя
    email_input = (By.XPATH, ".//label[text()='Email']/..//input") # поле почта
    password_input = (By.XPATH, ".//label[text()='Пароль']/..//input") # поле пароль
    button_checkinn = (By.XPATH, ".//button[text()='Зарегистрироваться']") #кнопка зарегестрироваться
    button_login = (By.XPATH, "//button[text()='Войти']") # войти в форме
    button_login_account = (By.XPATH, "//button[text()='Войти в аккаунт']") # войти на главной странице
    button_logout = (By.XPATH, "//button[text()='Выход']") # выйти
    text_recovery_pass = (By.XPATH, ".//a[text()='Восстановить пароль']") # текст восстановить пароль
    text_login = (By.XPATH, "//a[text()='Войти']") # текст войти
    text_personal_accaunt = (By.XPATH, "//p[text()='Личный Кабинет']") # текст личный кабинет
    text_checkin = (By.XPATH, "//a[text()='Зарегистрироваться']") # текст зарегестрироваться
    text_constructor = (By.XPATH, "//p[text()='Конструктор']") # текст конструктор
    text_get_burger = (By.XPATH, ".//h1[text()='Соберите бургер']") # текст соберите бургер
    text_rools = (By.XPATH, "//span[text()='Булки']") # текст булки
    text_sauces = (By.XPATH, "//span[text()='Соусы']") # текст соусы
    text_fillings = (By.XPATH, "//span[text()='Начинки']") # текст начинки
    img_1rools = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']") # картинка 1 булки
    img_1sauces = (By.XPATH, "//img[@alt='Соус Spicy-X']") # картинка 1 соуса
    img_1fillings = (By.XPATH, "//img[@alt='Мясо бессмертных моллюсков Protostomia']") # картинка 1-ой начинки
    invalid_pass_reg = (By.XPATH, ".//p[@class='input__error text_type_main-default']") # текст ошибки при неправильном пороле при регистрации
    logotip = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']") # главный логотип
    
    rolls_active = (By.XPATH, "//div[contains(@class, 'tab') and contains(@class, 'current') and .//span[text()='Булки']]")  # активный таб с названием «Булки».
    sauces_active = (By.XPATH, "//div[contains(@class, 'tab') and contains(@class, 'current') and .//span[text()='Соусы']]") # 
    fillings_active = (By.XPATH, "//div[contains(@class, 'tab') and contains(@class, 'current') and .//span[text()='Начинки']]") # 
    
    displayed_username = (By.XPATH, "//input[@name='Name' and contains(@class, 'input__textfield-disabled')]")
    # поиск по классу
    # Локаторы для проверки активного состояния


 