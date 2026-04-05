from selenium.webdriver.common.by import By
from pages.mExchange.base_page import BasePage
from pages.mPointShop.menu_page import MenuPage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[.//span[normalize-space()='Đăng nhập']]")

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.wait_url_contains("/#/dashboard")