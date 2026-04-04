import pytest
from drivers.driver_manager import DriverManager
@pytest.fixture
def driver(request,base_url):
    browser = request.config.getoption("--browser")
    driver = DriverManager.get_driver(browser)
    driver.base_url = base_url
    yield driver
    driver.quit()