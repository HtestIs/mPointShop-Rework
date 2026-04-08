import allure
import pytest

from mShopAdmin.pages.login_page import LoginPage
from mShopAdmin.pages.dashboard_page import DashboardPage


@pytest.fixture
def mshopadmin_base_url(env_config):
    return env_config["aap_base_url"]


@pytest.fixture
def login_aap_success(driver, env_config):
    login = LoginPage(driver)
    with allure.step("Logging in to mPointShop Admin Panel"):
        login.open_url()
        login.fill_login(
            env_config["aap_username"],
            env_config["aap_password"],
        )
    page = DashboardPage(driver)
    yield page
    with allure.step("Logging out mPointShop Admin Panel"):
        driver.delete_all_cookies()