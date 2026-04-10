from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from mPointApp.pages.base_screen import BaseScreen


class LoginScreen(BaseScreen):

    USERNAME_INPUT = (By.XPATH, "//android.widget.EditText[@text='Số điện thoại']")
    PASSWORD_INPUT = (By.XPATH, "//android.widget.EditText[@text='Nhập mật khẩu']")
    LOGIN_BUTTON = (By.XPATH, "//android.view.View")
    LOGIN_NOTIFICATION = (
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().className("android.widget.ScrollView").instance(1)'
)
    def login(self, username: str, password: str):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.tap(self.LOGIN_BUTTON)
    def message(self):
        message = self.get_text(self.LOGIN_NOTIFICATION)
        return message.strip()