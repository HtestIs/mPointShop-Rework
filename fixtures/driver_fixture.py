import os

import pytest

from core.drivers.driver_manager import DriverManager
from core.utils.token_helpers import get_local_storage_token
from mPointShop.pages.login_page import LoginPage
from mExchange.pages.login_page import LoginPage as ExchangeLoginPage

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    is_ci = os.getenv("CI", "").lower() == "true"
    cli_headless = request.config.getoption("--headless")
    driver = DriverManager.get_driver(
        browser,
        headless=cli_headless or is_ci
    )
    if request.node.get_closest_marker("mexchange"):
        base_url = request.getfixturevalue("mexchange_base_url")
    elif request.node.get_closest_marker("mshopadmin"):
        base_url = request.getfixturevalue("mshopadmin_base_url")
    else:
        base_url = request.getfixturevalue("mpointshop_base_url")

    driver.base_url = base_url
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def mexchange_token_from_ui(request, env_config):
    browser = request.config.getoption("--browser")
    cli_headless = request.config.getoption("--headless")
    is_ci = os.getenv("CI", "").lower() == "true"

    driver = DriverManager.get_driver(
        browser,
        headless=cli_headless or is_ci
    )
    try:
        login_page = ExchangeLoginPage(driver)
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

