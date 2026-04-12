from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from mPointApp.pages.base_screen import BaseScreen
from mPointApp.pages.password_screen import PasswordScreen


class OtpScreen(BaseScreen):
    PAGE_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NHẬP MÃ XÁC THỰC")')
    OTP_INPUT_FIELDS = (AppiumBy.XPATH,"//android.view.ViewGroup[@resource-id='OTPInputView']//android.widget.EditText")
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Tiếp tục")
    OTP_INPUT_FIRST_FIELD =(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("textInput").instance(0)')
    def click_continue(self):
        self.tap(self.CONTINUE_BUTTON)
        return PasswordScreen(self.driver)
    def is_otp_form_visible(self):
        return self.is_visible(self.PAGE_TITLE)
    def get_otp_inputs(self):
        return self.finds(self.OTP_INPUT_FIELDS)

    def enter_otp(self,otp):
        self.wait_visible(self.OTP_INPUT_FIRST_FIELD)
        inputs = self.get_otp_inputs()
        for box,digit in zip(inputs,otp):
            box.click()
            box.send_keys(digit)