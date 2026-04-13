import allure
import pytest

from mShopAdmin.api.client import MSHopAdminClient
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
    
@pytest.fixture
def mshopadmin_api_client(env_config):
    return MSHopAdminClient(base_url=env_config["aap_base_url"])

##Mshop Admin API client with token fixture, it using captcha, so we need to 
# set token in env file and use it in this fixture, not ideal but we can use
#  it for now until we find a better solution to handle captcha in tests.

@pytest.fixture
def mshopadmin_api_client_with_token(env_config, mshopadmin_api_client):
    token = env_config["aap_token"]
    if token:
        mshopadmin_api_client.set_token(token)
    return mshopadmin_api_client