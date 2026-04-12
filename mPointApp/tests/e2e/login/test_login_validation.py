import allure
import pytest

from mPointApp.pages.login_screen import LoginScreen


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@allure.feature("Login")
@allure.story("Credential validation")
@allure.title("Reject login with invalid credentials")
@allure.severity(allure.severity_level.NORMAL)
def test_login_with_invalid_credentials(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    login_screen.login(creds["app_username"], "123456789")
    assert login_screen.has_error_message("Thông tin đăng nhập không đúng,"), "Expected error message not found."


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@allure.feature("Login")
@allure.story("Field validation")
@allure.title("Require phone and password on login")
@allure.severity(allure.severity_level.NORMAL)
def test_login_with_empty_credentials(mobile_driver):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    login_screen.login("", "")
    assert login_screen.has_error_message("Vui lòng nhập số điện thoại"), "Expected error message not found."


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@allure.feature("Login")
@allure.story("Field validation")
@allure.title("Require password on login")
@allure.severity(allure.severity_level.NORMAL)
def test_login_with_empty_password(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    login_screen.login(creds["app_username"], "")
    assert login_screen.has_error_message("Vui lòng nhập mật khẩu"), "Expected error message not found."


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@allure.feature("Login")
@allure.story("Field validation")
@allure.title("Require phone number on login")
@allure.severity(allure.severity_level.NORMAL)
def test_login_with_empty_phone_number(mobile_driver):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    login_screen.login("", "123456789")
    assert login_screen.has_error_message("Vui lòng nhập số điện thoại"), "Expected error message not found."


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@allure.feature("Login")
@allure.story("Field validation")
@allure.title("Reject login with short password")
@allure.severity(allure.severity_level.NORMAL)
def test_login_with_short_password(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    login_screen.login(creds["app_username"], "123")
    assert login_screen.has_error_message("Mật khẩu phải có ít nhất 6 ký tự"), "Expected error message not found."

@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@pytest.mark.smoke
@allure.feature("Login")
@allure.story("Smoke")
@allure.title("Open app and validate phone format on login")
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_phone_number(mobile_driver):
    open_app = LoginScreen(mobile_driver)
    open_app.skip_intro()
    open_app.login("0123456789", "123456789")
    assert open_app.has_error_message("Vui lòng nhập số điện thoại hợp lệ"), "Expected error message not found."