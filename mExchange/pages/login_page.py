from selenium.webdriver.common.by import By

from mExchange.pages.base_page import BasePage
from mExchange.pages.menu_page import MenuPage


class LoginPage(BasePage):
    URL = "/#/login"
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[.//span[normalize-space()='Đăng nhập']]")

    def open_url(self):
        self.open(self.URL)

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.wait_url_contains("/#/dashboard")
        return MenuPage(self.driver)