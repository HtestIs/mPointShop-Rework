import pytest
import allure
from mPointApp.pages.login_screen import LoginScreen
@allure.feature("Registration")
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


@pytest.mark.parametrize("invalid_phone", ["09123456789", "1234567890", "abcdefghij","039484"],
                         ids=["Too long", "No prefix", "Non-numeric", "Too short"])
def test_registration_with_invalid_phone(mobile_driver, invalid_phone):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    register_screen = login_screen.click_register()
    register_screen.enter_phone_number(invalid_phone)
    register_screen.accept_terms()
    register_screen.click_continue()
    assert register_screen.has_error_message("Vui lòng nhập số điện thoại hợp lệ"), f"Expected error message not found."

def test_registration_without_accepting_terms(mobile_driver, user_data):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    register_screen = login_screen.click_register()
    data = user_data.copy()
    register_screen.enter_phone_number(data["phone_number"])
    register_screen.click_continue()
    assert not register_screen.continue_button_is_enabled(), "Continue button should be disabled when terms are not accepted."

def test_registration_with_empty_phone_number(mobile_driver):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    register_screen = login_screen.click_register()
    register_screen.enter_phone_number("")
    register_screen.accept_terms()
    register_screen.click_continue()
    assert register_screen.has_error_message("Vui lòng nhập số điện thoại"), f"Expected error message not found."

def test_registration_with_existing_phone_number(mobile_driver, env_config):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    register_screen = login_screen.click_register()
    register_screen.enter_phone_number(env_config["app_username"])
    register_screen.accept_terms()
    register_screen.click_continue()
    assert register_screen.has_error_message("Số điện thoại đã được đăng ký"), f"Expected error message not found."
