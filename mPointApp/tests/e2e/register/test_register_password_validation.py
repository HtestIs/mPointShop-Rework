import allure
import pytest

from mPointApp.flows.register_prerequisite import RegisterFlow


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.registration
@allure.feature("Registration")
@allure.story("Password validation")
@allure.title("Reject registration when password confirmation does not match")
@allure.severity(allure.severity_level.NORMAL)
def test_password_mismatch_during_registration(mobile_driver, user_data):
    data = user_data.copy()
    password_screen = RegisterFlow(mobile_driver).go_to_password_creation_screen(data["phone_number"], "44444")
    password_screen.enter_password(data["password"])
    password_screen.enter_confirm_password("different_password")
    password_screen.click_confirm()
    assert password_screen.has_error_message("Mật khẩu xác nhận không khớp"), "Expected error message not found."


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.registration
@allure.feature("Registration")
@allure.story("Password validation")
@allure.title("Reject registration when password is too short")
@allure.severity(allure.severity_level.NORMAL)
def test_registration_with_weak_password(mobile_driver, user_data):
    data = user_data.copy()
    password_screen = RegisterFlow(mobile_driver).go_to_password_creation_screen(data["phone_number"], "44444")
    password_screen.enter_password("123")
    password_screen.enter_confirm_password("123")
    password_screen.click_confirm()
    assert password_screen.has_error_message("Mật khẩu phải có ít nhất 6 ký tự"), "Expected error message not found."


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.registration
@allure.feature("Registration")
@allure.story("Password validation")
@allure.title("Reject registration when password exceeds allowed length")
@allure.severity(allure.severity_level.NORMAL)
def test_registration_with_long_password(mobile_driver, user_data):
    data = user_data.copy()
    password_screen = RegisterFlow(mobile_driver).go_to_password_creation_screen(data["phone_number"], "44444")
    long_password = "1" * 51
    password_screen.enter_password(long_password)
    password_screen.enter_confirm_password(long_password)
    password_screen.click_confirm()
    assert password_screen.has_error_message("Mật khẩu chỉ được phép 6 ký tự"), "Expected error message not found."


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.registration
@allure.feature("Registration")
@allure.story("Password validation")
@allure.title("Reject registration when password is not numeric")
@allure.severity(allure.severity_level.NORMAL)
def test_registration_with_non_numeric_password(mobile_driver, user_data):
    data = user_data.copy()
    password_screen = RegisterFlow(mobile_driver).go_to_password_creation_screen(data["phone_number"], "44444")
    password_screen.enter_password("abcdef")
    password_screen.enter_confirm_password("abcdef")
    password_screen.click_confirm()
    assert password_screen.has_error_message("Mật khẩu có 6 ký tự là số"), "Expected error message not found."