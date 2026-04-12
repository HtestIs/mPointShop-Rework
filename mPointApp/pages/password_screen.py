from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from mPointApp.pages.base_screen import BaseScreen
from mPointApp.pages.home_screen import AppHomePage
from mPointApp.pages.system.phone_dialog_page import AndroidPermissionDialog


class PasswordScreen(BaseScreen):
    PAGE_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("TẠO MẬT KHẨU MỚI")')
    PASSWORD_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nhập mật khẩu")')
    CONFIRM_PASSWORD_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nhập lại mật khẩu")')
    CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Xác nhận")

    def is_password_screen_visible(self):
        return self.is_visible(self.PAGE_TITLE)
    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)
    def enter_confirm_password(self, password):
        self.type_text(self.CONFIRM_PASSWORD_INPUT, password)
    def click_confirm(self):
        self.tap(self.CONFIRM_BUTTON)
        return AndroidPermissionDialog(self.driver)