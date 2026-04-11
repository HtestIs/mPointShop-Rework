from faker.generator import random
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from mPointApp.pages.base_screen import BaseScreen
from mPointApp.pages.register_screen import RegisterScreen


class LoginScreen(BaseScreen):

    SKIP_INTRO_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Bỏ qua")
    USERNAME_INPUT = (By.XPATH, "//android.widget.EditText[@hint='Số điện thoại']")
    PASSWORD_INPUT = (By.XPATH, "//android.widget.EditText[@hint='Nhập mật khẩu']")
    LOGIN_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='Đăng nhập']")

    CLOSE_ALERT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Đóng")')
    FORGOT_PASSWORD_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Quên mật khẩu")
    REGISTER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Đăng ký")')
    def skip_intro(self):
        self.tap(self.SKIP_INTRO_BUTTON)
    def login(self, username: str, password: str):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.tap(self.LOGIN_BUTTON)
    def close_alert(self):
        self.tap(self.CLOSE_ALERT_BUTTON)
    def is_forgot_password_visible(self):
        return self.is_visible(self.FORGOT_PASSWORD_BUTTON)
    def multiple_attempt_login(self, username, password, attempts=None):
        if not attempts:
            attempts = random.randint(0, 3)  # Randomly choose between 0 to 3 attempts
        for _ in range(attempts):
            self.login(username, password)
            self.close_alert()
        return attempts
    
    def click_register(self):
        self.tap(self.REGISTER_BUTTON)
        return RegisterScreen(self.driver)
