import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from mPointApp.pages.login_screen import LoginScreen


@pytest.fixture
def mobile_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.mediaone.mKafe"
    options.app_activity = "com.mediaone.mKafe.MainActivity"
    options.udid = "emulator-5554"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_valid_user(mobile_driver, env_config):
    creds = env_config
    mobile_driver.implicitly_wait(10)
    login_screen = LoginScreen(mobile_driver)
    login_screen.skip_intro()
    dialog = login_screen.login(creds["app_username"], creds["app_password"])
    return dialog.allow_permission()