import allure
import pytest

from mPointApp.pages.login_screen import LoginScreen


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@allure.feature("Login")
@allure.story("Lockout")
@allure.title("Show failed-attempt counter after repeated invalid logins")
@allure.severity(allure.severity_level.CRITICAL)
def test_multiple_failed_login_attempts(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    attempts = login_screen.multiple_attempt_login(creds["app_username"], "wrongpassword")
    login_screen.login(creds["app_username"], "wrongpassword")
    assert login_screen.has_error_message(
        f"Số lần đăng nhập sai: {attempts + 1}/5"
    ), f"Expected error message for {attempts + 1} failed attempts not found."


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@allure.feature("Login")
@allure.story("Lockout")
@allure.title("Show lockout guidance at maximum failed attempts")
@allure.severity(allure.severity_level.CRITICAL)
def test_maximum_failed_login_attempts(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    attempts = login_screen.multiple_attempt_login(creds["app_username"], "wrongpassword", attempts=4)
    login_screen.login(creds["app_username"], "wrongpassword")
    assert login_screen.has_error_message("Vui lòng kiểm tra lại thông tin hoặc đặt lại mật khẩu"), (
        f"Expected account lockout message not found after {attempts + 1} failed attempts."
    )
    assert login_screen.is_forgot_password_visible(), (
        "Forgot Password option should be visible after account lockout."
    )


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@allure.feature("Login")
@allure.story("Lockout")
@allure.title("Keep account locked when attempts exceed maximum")
@allure.severity(allure.severity_level.CRITICAL)
def test_exceed_maximum_failed_login_attempts(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    attempts = login_screen.multiple_attempt_login(creds["app_username"], "wrongpassword", attempts=5)
    login_screen.login(creds["app_username"], "wrongpassword")
    assert login_screen.has_error_message("Vui lòng kiểm tra lại thông tin hoặc đặt lại mật khẩu"), (
        f"Expected account lockout message not found after {attempts + 1} failed attempts."
    )
    assert login_screen.is_forgot_password_visible(), (
        "Forgot Password option should be visible after account lockout."
    )


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@allure.feature("Login")
@allure.story("Lockout")
@allure.title("Reset failed-attempt counter when credentials change")
@allure.severity(allure.severity_level.NORMAL)
def test_changing_credentials_after_failed_attempts(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    login_screen.multiple_attempt_login(creds["app_username"], "wrongpassword", attempts=3)
    login_screen.login("012345678", creds["app_password"])
    assert login_screen.has_error_message("Số lần đăng nhập sai: 1/5"), (
        "Expected error message for 1 failed attempt not found after changing credentials."
    )