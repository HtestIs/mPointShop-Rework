from mPointApp.pages.login_screen import LoginScreen
import pytest

@pytest.mark.defect
def test_open_app(mobile_driver):
    open_app = LoginScreen(mobile_driver)
    open_app.skip_intro()
    open_app.login("0123456789", "123456789")
    assert open_app.has_error_message("Vui lòng nhập số điện thoại hợp lệ"), f"Expected error message not found."

@pytest.mark.defect
def test_login_with_invalid_credentials(mobile_driver,env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    login_screen.login(creds["app_username"], "123456789")
    assert login_screen.has_error_message("Thông tin đăng nhập không đúng,"), f"Expected error message not found."

@pytest.mark.defect
def test_login_with_empty_credentials(mobile_driver):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    login_screen.login("", "")
    assert login_screen.has_error_message("Vui lòng nhập số điện thoại"), f"Expected error message not found."

@pytest.mark.defect
def test_login_with_empty_password(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    login_screen.login(creds["app_username"], "")
    assert login_screen.has_error_message("Vui lòng nhập mật khẩu"), f"Expected error message not found."

@pytest.mark.defect
def test_login_with_empty_phone_number(mobile_driver):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    login_screen.login("", "123456789")
    assert login_screen.has_error_message("Vui lòng nhập số điện thoại"), f"Expected error message not found."

@pytest.mark.defect
def test_login_with_short_password(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    login_screen.login(creds["app_username"], "123")
    assert login_screen.has_error_message("Mật khẩu phải có ít nhất 6 ký tự"), f"Expected error message not found."

@pytest.mark.defect
def test_multiple_failed_login_attempts(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    attempts =login_screen.multiple_attempt_login(creds["app_username"], "wrongpassword")
    login_screen.login(creds["app_username"], "wrongpassword")
    login_screen.has_error_message(f"Số lần đăng nhập sai: {attempts+1}/5"), f"Expected error message for {attempts+1} failed attempts not found."

@pytest.mark.defect
def test_maximum_failed_login_attempts(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    attempts = login_screen.multiple_attempt_login(creds["app_username"], "wrongpassword", attempts=4)
    login_screen.login(creds["app_username"], "wrongpassword")
    assert login_screen.has_error_message("Vui lòng kiểm tra lại thông tin hoặc đặt lại mật khẩu"), f"Expected account lockout message not found after {attempts+1} failed attempts."
    assert login_screen.is_forgot_password_visible(), "Forgot Password option should be visible after account lockout."

@pytest.mark.defect
def test_exceed_maximum_failed_login_attempts(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    attempts = login_screen.multiple_attempt_login(creds["app_username"], "wrongpassword", attempts=5)
    login_screen.login(creds["app_username"], "wrongpassword")
    assert login_screen.has_error_message("Vui lòng kiểm tra lại thông tin hoặc đặt lại mật khẩu"), f"Expected account lockout message not found after {attempts+1} failed attempts."
    assert login_screen.is_forgot_password_visible(), "Forgot Password option should be visible after account lockout."

@pytest.mark.defect
def test_changing_credentials_after_failed_attempts(mobile_driver, env_config):
    creds = env_config
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    attempts = login_screen.multiple_attempt_login(creds["app_username"], "wrongpassword", attempts=3)
    login_screen.login("012345678", creds["app_password"])
    assert login_screen.has_error_message(f"Số lần đăng nhập sai: 1/5"), f"Expected error message for 1 failed attempt not found after changing credentials."
