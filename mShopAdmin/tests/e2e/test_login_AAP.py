import allure
import pytest

from mShopAdmin.pages.login_page import LoginPage
from time import sleep
pytestmark = [
    pytest.mark.mshopadmin,
    allure.parent_suite("mShopAdmin"),
    allure.suite("E2E"),
    allure.sub_suite("Authentication"),
]

@pytest.mark.defect
@allure.story("AAP login")
@allure.title("Login with valid AAP credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_valid_aap(driver, env_config):
    login_page = LoginPage(driver)
    login_page.open_url()
    sleep(5)
    login_page.fill_login(env_config["aap_username"], env_config["aap_password"])
    assert "/#/dashboard" in login_page.get_current_url(), "User is not redirected to dashboard after login"

@pytest.mark.defect
@allure.story("AAP login")
@allure.title("Login with invalid AAP password shows error")
@allure.severity(allure.severity_level.NORMAL)
def test_login_invalid_aap(driver, env_config):
    login_page = LoginPage(driver)
    login_page.open_url()
    login_page.fill_login(env_config["aap_username"], "wrong_password")
    assert "Sai tên đăng nhập hoặc mật khẩu" in login_page.get_error_message(), "Error message not displayed for invalid login"

@pytest.mark.defect
@allure.story("AAP login")
@allure.title("Login with empty AAP fields shows validation")
@allure.severity(allure.severity_level.NORMAL)
def test_login_empty_fields_aap(driver):
    login_page = LoginPage(driver)
    login_page.open_url()
    login_page.fill_login("", "")
    assert "Vui lòng nhập" in login_page.get_username_alert(), "Error message not displayed for empty username"
    assert "Vui lòng nhập" in login_page.get_password_alert(), "Error message not displayed for empty password"

@pytest.mark.defect
@allure.story("AAP login")
@allure.title("AAP login rejects SQL injection input")
@allure.severity(allure.severity_level.CRITICAL)
def test_sql_injection_aap(driver, env_config):
    login_page = LoginPage(driver)
    login_page.open_url()
    login_page.fill_login("' OR '1'='1", "' OR '1'='1")
    assert "Sai tên đăng nhập hoặc mật khẩu" in login_page.get_error_message(), "Error message not displayed for SQL injection attempt"

