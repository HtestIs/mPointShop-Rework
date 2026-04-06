import pytest

from core.drivers.driver_manager import DriverManager
from core.utils.token_helpers import get_local_storage_token
from mExchange.pages.login_page import LoginPage


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    driver = DriverManager.get_driver(browser)

    if request.node.get_closest_marker("mexchange"):
        base_url = request.getfixturevalue("mexchange_base_url")
    else:
        base_url = request.getfixturevalue("mpointshop_base_url")

    driver.base_url = base_url
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def mexchange_token_from_ui(request, env_config):
    browser = request.config.getoption("--browser")
    driver = DriverManager.get_driver(browser)
    try:
        login_page = LoginPage(driver)
        login_page.open(env_config["mexchange_web_url"])
        login_page.login(
            env_config["mexchange_username"],
            env_config["mexchange_password"]
        )

        token = get_local_storage_token(driver, key="token")
        if not token:
            raise AssertionError("Failed to get mExchange token from localStorage")

        return token
    finally:
        driver.quit()