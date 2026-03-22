import pytest
from config.env_config import ENV_CONFIG
from pages.login_page import LoginPage
from pages.voucher_scan_page import VoucherScan
from pages.store_manage_page import StoreManage
import os
from datetime import datetime
import allure
pytest_plugins = [
    "fixtures.driver_fixture",
    "data.store_data"
]
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--env", action="store",default="dev")
@pytest.fixture
def env(request):
    return request.config.getoption("--env")
@pytest.fixture
def env_config(env):
    return ENV_CONFIG[env]
@pytest.fixture
def base_url(request,env_config):
    return env_config["base_url"]
@pytest.fixture
def login_merchant_success(driver,base_url,env_config):
    login = LoginPage(driver)
    creds = env_config["users"]["merchant"]
    with allure.step("Logging in as merchant"):
        login.open_url(base_url)
        login.fill_login(creds["username"], creds["password"])
    page = VoucherScan(driver)
    yield page
    with allure.step("Logging out merchant"):
        driver.delete_all_cookies()
@pytest.fixture
def login_partner_success(driver,base_url,env_config):
    login = LoginPage(driver)
    creds = env_config["users"]["partner"]
    with allure.step("Logging in as partner"):
        login = LoginPage(driver)
        login.open_url(base_url)
        login.fill_login(creds["username"], creds["password"])
    page = StoreManage(driver)
    yield page
    with allure.step("Logging out partner"):
        driver.delete_all_cookies()
@pytest.fixture
def get_dup_username(env_config):
    return env_config["dup_username"]
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call":
        return
    driver = item.funcargs.get("driver",None)
    if report.failed and driver:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Create allure attachments for screenshot, page source, and current URL
        allure.attach(driver.get_screenshot_as_png(),name=f"screenshot_{timestamp}.png",attachment_type=allure.attachment_type.PNG)
        allure.attach(driver.page_source,name=f"page_source_{timestamp}.html",attachment_type=allure.attachment_type.HTML)
        allure.attach(driver.current_url,name=f"current_url",attachment_type=allure.attachment_type.TEXT)
        # Create allure attachments for logs if available
        try:
            logs = driver.get_log("browser")
            if logs:
                allure.attach(str(logs),name=f"browser_logs",attachment_type=allure.attachment_type.TEXT)
        except Exception:
            pass