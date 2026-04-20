from pages.base_page import BasePage

class MainPage(BasePage):
    def open(self, url):
        self.driver.get(url)