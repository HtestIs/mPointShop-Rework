import os

import allure
import pytest

from core.drivers.driver_manager import DriverManager
from core.utils.token_helpers import get_local_storage_token
from mExchange.api.client import MExchangeClient
from mExchange.api.endpoints.user_api import ExchangeAuthAPI
from mExchange.pages.login_page import LoginPage
from mExchange.pages.menu_page import MenuPage

@pytest.fixture
def mexchange_base_url(env_config):
    return env_config["mexchange_web_url"]


@pytest.fixture
def mexchange_client(env_config):
    return MExchangeClient(base_url=env_config["mexchange_api_url"])


@pytest.fixture
def mexchange_auth_api(mexchange_client_ui):
    return ExchangeAuthAPI(mexchange_client_ui)




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
