import allure
import pytest

from mPointApp.pages.login_screen import LoginScreen


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@pytest.mark.registration
@allure.feature("Registration")
@allure.story("OTP validation")
@allure.title("Reject registration with invalid OTP")
@allure.severity(allure.severity_level.NORMAL)
def test_registration_with_invalid_otp(mobile_driver, user_data):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    register_screen = login_screen.click_register()

    data = user_data.copy()
    register_screen.enter_phone_number(data["phone_number"])
    register_screen.accept_terms()

    otp_screen = register_screen.click_continue()
    otp_screen.enter_otp("1234")
    otp_screen.click_continue()
    assert otp_screen.has_error_message("Sai mã OTP"), "Expected error message not found."


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.registration
@allure.feature("Registration")
@allure.story("OTP validation")
@allure.title("Require OTP during registration")
@allure.severity(allure.severity_level.NORMAL)
def test_registration_with_empty_otp(mobile_driver, user_data):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    register_screen = login_screen.click_register()

    data = user_data.copy()
    register_screen.enter_phone_number(data["phone_number"])
    register_screen.accept_terms()

    otp_screen = register_screen.click_continue()
    otp_screen.click_continue()
    assert otp_screen.has_error_message("Vui lòng nhập mã OTP"), "Expected error message not found."