from pages.mPointShop.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
class LoginPage(BasePage):
    TEXT_USERNAME = (By.XPATH,"//input[@placeholder='Tên đăng nhập']")
    TEXT_PASSWORD = (By.XPATH,"//input[@placeholder='Mật khẩu']")
    BUTTON_LOGIN = (By.XPATH,"//button[.//span[normalize-space()='Đăng nhập']]")
    TOAST_MESSAGE =(By.XPATH,"//div[@role='alert']//div[last()]")
    NAV_BAR = (By.ID,"cheader")
    URL = '/login'
    @allure.step("Open login page")
    def open_url(self):
        self.open(self.URL)
    @allure.step("Enter username: {username}")
    def enter_username(self,username):
        self.type_text(self.TEXT_USERNAME,username)
    @allure.step("Enter password")
    def enter_password(self,password):
        self.type_text(self.TEXT_PASSWORD,password)
    @allure.step("Fill login form with username: {username}")
    def fill_login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click(self.BUTTON_LOGIN)
    @allure.step("Get toast message")
    def get_toast_message(self):
        return self.get_text(self.TOAST_MESSAGE)
    def fill_login_success(self,username,password):
        self.fill_login(username,password)
        self.wait_login_page_loaded()
    def wait_login_page_loaded(self):
        self.wait_visible(self.NAV_BAR)
 
