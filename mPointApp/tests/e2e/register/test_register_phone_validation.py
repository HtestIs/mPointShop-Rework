import allure
import pytest

from mPointApp.pages.login_screen import LoginScreen


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.registration
@pytest.mark.defect
@pytest.mark.parametrize(
    "invalid_phone",
    ["09123456789", "1234567890", "abcdefghij", "039484"],
    ids=["Too long", "No prefix", "Non-numeric", "Too short"],
)
@allure.feature("Registration")
@allure.story("Phone validation")
@allure.title("Reject registration for invalid phone formats")
@allure.severity(allure.severity_level.NORMAL)
def test_registration_with_invalid_phone(mobile_driver, invalid_phone):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    register_screen = login_screen.click_register()
    register_screen.enter_phone_number(invalid_phone)
    register_screen.accept_terms()
    register_screen.click_continue()
    assert register_screen.has_error_message("Vui lòng nhập số điện thoại hợp lệ"), "Expected error message not found."


@pytest.mark.mpointapp
@pytest.mark.defect
@pytest.mark.e2e
@pytest.mark.registration
@allure.feature("Registration")
@allure.story("Phone validation")
@allure.title("Disable continue when terms are not accepted")
@allure.severity(allure.severity_level.NORMAL)
def test_registration_without_accepting_terms(mobile_driver, user_data):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    register_screen = login_screen.click_register()

    data = user_data.copy()
    register_screen.enter_phone_number(data["phone_number"])
    register_screen.click_continue()
    assert not register_screen.continue_button_is_enabled(), (
        "Continue button should be disabled when terms are not accepted."
    )


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@pytest.mark.registration
@allure.feature("Registration")
@allure.story("Phone validation")
@allure.title("Require phone number during registration")
@allure.severity(allure.severity_level.NORMAL)
def test_registration_with_empty_phone_number(mobile_driver):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    register_screen = login_screen.click_register()
    register_screen.enter_phone_number("")
    register_screen.accept_terms()
    register_screen.click_continue()
    assert register_screen.has_error_message("Vui lòng nhập số điện thoại"), "Expected error message not found."


@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@pytest.mark.registration
@allure.feature("Registration")
@allure.story("Phone validation")
@allure.title("Reject registration for an existing phone number")
@allure.severity(allure.severity_level.NORMAL)
def test_registration_with_existing_phone_number(mobile_driver, env_config):
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    register_screen = login_screen.click_register()
    register_screen.enter_phone_number(env_config["app_username"])
    register_screen.accept_terms()
    register_screen.click_continue()
    assert register_screen.has_error_message("Số điện thoại đã được đăng ký"), "Expected error message not found."