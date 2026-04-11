from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from mPointApp.pages.base_screen import BaseScreen
from mPointApp.pages.otp_screen import OtpScreen



class RegisterScreen(BaseScreen):
    # Define locators for registration screen elements here
    REGISTER_PHONE_NUMBER= (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Số điện thoại")')
    TOS_CHECKBOX = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(16)')
    CONTINUE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Tiếp tục")')
    
    ##DO LATER
    def enter_phone_number(self, phone_number: str):
        self.type_text(self.REGISTER_PHONE_NUMBER, phone_number)
    def accept_terms(self):
        self.tap(self.TOS_CHECKBOX)
    def click_continue(self):
        self.tap(self.CONTINUE_BUTTON)
        return OtpScreen(self.driver)
    def continue_button_is_enabled(self):
        continue_button = self.find(self.CONTINUE_BUTTON)
        return continue_button.is_enabled()
