import allure
import pytest

from core.drivers.driver_manager import DriverManager
from core.utils.token_helpers import get_local_storage_token
from mExchange.pages.login_page import LoginPage
from mExchange.pages.menu_page import MenuPage


@pytest.fixture
def mexchange_base_url(env_config):
    return env_config["mexchange_web_url"]


@pytest.fixture(scope="session")
def mexchange_token_from_ui(request, env_config):
    browser = request.config.getoption("--browser")
    driver = DriverManager.get_driver(browser)
    try:
        login_page = LoginPage(driver)
        login_page.open(env_config["mexchange_web_url"])
        login_page.login(
            env_config["mexchange_username"],
            env_config["mexchange_password"],
        )

        token = get_local_storage_token(driver, key="token")
        if not token:
            raise AssertionError("Failed to get mExchange token from localStorage")

        return token
    finally:
        driver.quit()


@pytest.fixture
def login_mexchange_success(driver, env_config):
    login = LoginPage(driver)
    with allure.step("Logging in to mExchange"):
        login.open_url()
        login.login(
            env_config["mexchange_username"],
            env_config["mexchange_password"],
        )
    page = MenuPage(driver)
    yield page
    with allure.step("Logging out mExchange"):
        driver.delete_all_cookies()
