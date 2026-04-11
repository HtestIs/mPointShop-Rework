from mPointApp.pages.login_screen import LoginScreen
from mPointApp.pages.otp_screen import OtpScreen
from mPointApp.pages.password_screen import PasswordScreen
from mPointApp.pages.register_screen import RegisterScreen


class RegisterFlow:
    def __init__(self, driver):
        self.driver = driver
        self.login_screen = LoginScreen(driver)
        self.register_screen = RegisterScreen(driver)
        self.otp_screen = OtpScreen(driver)
        self.password_screen = PasswordScreen(driver)
    def go_to_password_creation_screen(self,phone_number,otp):
        self.login_screen.skip_intro()
        self.login_screen.click_register()
        self.register_screen.enter_phone_number(phone_number)
        self.register_screen.accept_terms()
        self.register_screen.click_continue()
        self.otp_screen.enter_otp(otp)
        return self.otp_screen.click_continue()