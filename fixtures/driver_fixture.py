import pytest
from drivers.driver_manager import DriverManager
from pages.mExchange.login_page import LoginPage
from utils.token_helpers import get_local_storage_token
@pytest.fixture()
def driver(request,base_url):
    browser = request.config.getoption("--browser")
    driver = DriverManager.get_driver(browser)
    driver.base_url = base_url
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def mexchange_bootstrap_driver(request):
    browser = request.config.getoption("--browser")
    driver = DriverManager.get_driver(browser)
    yield driver
    driver.quit()
@pytest.fixture(scope="session")
def mexchange_token_from_ui(mexchange_bootstrap_driver, env_config):
    login_page = LoginPage(mexchange_bootstrap_driver)

    login_page.open(env_config["mexchange_web_url"])
    login_page.login(
        env_config["mexchange_username"],
        env_config["mexchange_password"]
    )
    token = get_local_storage_token(mexchange_bootstrap_driver, key="token")
    if not token:
        raise AssertionError("Failed to get mExchange token from localStorage")

    return token