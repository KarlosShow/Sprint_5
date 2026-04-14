from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MainPage:
# инициализировать драйвер сохраняя ссылку на драйвер и создать обьект ожидания
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
# открыть страницу указанную
    def open(self, url):
        self.driver.get(url)
# найти элемент по переданному локатору
    def find(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))
# нажать на найденный элемент
    def click(self, locator):
        self.find(locator).click()
# ввести свои данные в найденное поле
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
# получить текст с элемента
    def get_text(self, locator):
        return self.find(locator).text
# скролл до нужного элемента    
    def get_attribute_value(self, locator, attribute_name):
        return self.find(locator).get_attribute(attribute_name)  
# поиск видимости элемента
    def element_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))
    