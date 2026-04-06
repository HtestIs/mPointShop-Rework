import allure
import pytest

from mExchange.pages.login_page import LoginPage
from mExchange.pages.menu_page import MenuPage


@pytest.fixture
def mexchange_base_url(env_config):
    return env_config["mexchange_web_url"]


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
