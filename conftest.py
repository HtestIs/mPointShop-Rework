from datetime import datetime

import allure
import pytest

from config.env_config import ENV_CONFIG

pytest_plugins = [
    "data.store_data",
    "data.voucher_data",
    "fixtures.driver_fixture",
    "fixtures.shared_api_fixtures",
    "fixtures.shared_voucher_fixtures",
    "data.end_user_data",
]


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--env", action="store", default="dev")
    parser.addoption("--headless", action="store_true", default=False)

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def env_config(env):
    return ENV_CONFIG[env]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call":
        return

    driver = item.funcargs.get("driver", None)
    if report.failed and driver:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"screenshot_{timestamp}.png",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            driver.page_source,
            name=f"page_source_{timestamp}.html",
            attachment_type=allure.attachment_type.HTML,
        )
        allure.attach(
            driver.current_url,
            name="current_url",
            attachment_type=allure.attachment_type.TEXT,
        )
        try:
            logs = driver.get_log("browser")
            if logs:
                allure.attach(
                    str(logs),
                    name="browser_logs",
                    attachment_type=allure.attachment_type.TEXT,
                )
        except Exception:
            pass