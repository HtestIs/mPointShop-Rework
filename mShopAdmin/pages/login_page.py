from mShopAdmin.pages.basepage import BasePage
from selenium.webdriver.common.by import By
import allure
class LoginPage(BasePage):
    URL = "/#/signin"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and .//span[normalize-space()='Đăng nhập']]")
    USERNAME_ALERT = (By.XPATH,"//input[@id='username']/ancestor::div[contains(@class,'ant-form-item')]//div[@role='alert' and normalize-space()='Vui lòng nhập tên tài khoản!']")
    PASSWORD_ALERT = (By.XPATH,"//input[@id='password']/ancestor::div[contains(@class,'ant-form-item')]//div[@role='alert' and normalize-space()='Vui lòng nhập mật khẩu!']")
    LOGIN_ERROR_TEXT = (By.XPATH,"//div[contains(@class,'ant-message-error')]//span[normalize-space()='Sai tên đăng nhập hoặc mật khẩu']")
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

    def get_username_alert(self):
        self.wait_visible(self.USERNAME_ALERT)
        return self.find(self.USERNAME_ALERT).text
    
    def get_password_alert(self):
        self.wait_visible(self.PASSWORD_ALERT)
        return self.find(self.PASSWORD_ALERT).text
    
    def get_error_message(self):
        self.wait_visible(self.LOGIN_ERROR_TEXT)
        return self.find(self.LOGIN_ERROR_TEXT).text