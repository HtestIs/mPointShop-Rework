import pytest
from config.env_config import ENV_CONFIG
from pages.login_page import LoginPage
from pages.voucher_scan_page import VoucherScan
from pages.store_manage_page import StoreManage
import os
from datetime import datetime
pytest_plugins = [
    "fixtures.driver_fixture",
    "fixtures.store_data"
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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver",None)
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir,exist_ok=True)
            file_path = f"{screenshot_dir}/{test_name}_{timestamp}.png"
            driver.save_screenshot(file_path)