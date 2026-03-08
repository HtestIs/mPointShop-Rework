import pytest
from config.env_config import ENV_CONFIG
from pages.login_page import LoginPage
from pages.voucher_scan_page import VoucherScan
from pages.store_manage_page import StoreManage
pytest_plugins = [
    "fixtures.driver_fixture"
]
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--env", action="store",default="dev")

@pytest.fixture
def base_url(request):
    env = request.config.getoption("--env")
    return ENV_CONFIG[env]

@pytest.fixture
def login_merchant_success(driver,base_url):
    login = LoginPage(driver)
    login.open_url(base_url)
    login.fill_login("craftmbeer_1","123456789")
    return VoucherScan(driver)
@pytest.fixture
def login_partner_success(driver,base_url):
    login = LoginPage(driver)
    login.open_url(base_url)
    login.fill_login("mbeer_partner","123456789")
    return StoreManage(driver)