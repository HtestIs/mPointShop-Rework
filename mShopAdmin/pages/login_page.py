from mShopAdmin.pages.basepage import BasePage
from selenium.webdriver.common.by import By
import allure
class LoginPage(BasePage):
    URL = "/#/signin"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and .//span[normalize-space()='Đăng nhập']]")

    @allure.step("Open login page")
    def open_url(self):
        self.open(self.URL)
    
    def type_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)

    def type_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)
    
    @allure.step("Fill login form with username: {username} and password: {password}")
    def fill_login(self, username, password):
        self.type_username(username)
        self.type_password(password)
        self.click(self.LOGIN_BUTTON)
        self.wait_url_contains("dashboard")