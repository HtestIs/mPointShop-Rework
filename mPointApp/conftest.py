import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def mobile_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.mediaone.mKafe"
    options.app_activity = "com.mediaone.mKafe.MainActivity"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()