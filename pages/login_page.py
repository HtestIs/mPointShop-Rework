from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    TEXT_USERNAME = (By.XPATH,"//input[@placeholder='Tên đăng nhập']")
    TEXT_PASSWORD = (By.XPATH,"//input[@placeholder='Mật khẩu']")
    BUTTON_LOGIN = (By.XPATH,"//button[.//span[normalize-space()='Đăng nhập']]")
    TOAST_MESSAGE =(By.XPATH,"//div[@role='alert']//div[last()]")
    URL = '/login'
    def open_url(self,base_url):
        self.open(base_url + self.URL)
    def enter_username(self,username):
        self.type_text(self.TEXT_USERNAME,username)
    def enter_password(self,password):
        self.type_text(self.TEXT_PASSWORD,password)
    def fill_login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click(self.BUTTON_LOGIN)
    def get_toast_message(self):
        return self.get_text(self.TOAST_MESSAGE)
 
