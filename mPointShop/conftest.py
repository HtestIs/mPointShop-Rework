import allure
import pytest

from mPointShop.pages.login_page import LoginPage
from mPointShop.pages.menu_page import MenuPage


@pytest.fixture
def mpointshop_base_url(env_config):
    return env_config["base_url"]


@pytest.fixture
def login_merchant_success(driver, env_config):
    login = LoginPage(driver)
    creds = env_config["users"]["merchant"]
    with allure.step("Logging in as merchant"):
        login.open_url()
        login.fill_login_success(creds["username"], creds["password"])
    page = MenuPage(driver)
    yield page
    with allure.step("Logging out merchant"):
        driver.delete_all_cookies()
@pytest.fixture
def login_valid_merchant_success(driver, env_config):
    login = LoginPage(driver)
    creds = env_config["users"]["valid_merchant"]
    with allure.step("Logging in as valid merchant"):
        login.open_url()
        login.fill_login_success(creds["username"], creds["password"])
    page = MenuPage(driver)
    yield page
    with allure.step("Logging out valid merchant"):
        driver.delete_all_cookies()

@pytest.fixture
def login_partner_success(driver, env_config):
    login = LoginPage(driver)
    creds = env_config["users"]["partner"]
    with allure.step("Logging in as partner"):
        login.open_url()
        login.fill_login_success(creds["username"], creds["password"])
    page = MenuPage(driver)
    yield page
    with allure.step("Logging out partner"):
        driver.delete_all_cookies()


@pytest.fixture
def get_dup_username(env_config):
    return env_config["dup_username"]
