import allure
import pytest

from mPointApp.pages.login_screen import LoginScreen


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.registration
@allure.feature("Registration")
@allure.story("Happy path")
@allure.title("Register successfully with valid phone, OTP, and password")
@allure.severity(allure.severity_level.CRITICAL)
def test_registration_flow(mobile_driver, user_data):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    register_screen = login_screen.click_register()

    data = user_data.copy()
    register_screen.enter_phone_number(data["phone_number"])
    register_screen.accept_terms()

    otp_screen = register_screen.click_continue()
    otp_screen.enter_otp("44444")

    password_screen = otp_screen.click_continue()
    password_screen.enter_password(data["password"])
    password_screen.enter_confirm_password(data["password"])

    home_screen = password_screen.click_confirm()
    assert home_screen.is_homepage_displayed(), "Home screen should be visible after successful registration."
    assert home_screen.is_navigated_to_homepage(), "Should navigate to homepage after registration."