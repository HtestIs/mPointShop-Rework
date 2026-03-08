import pytest
from drivers.driver_manager import DriverManager
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = DriverManager.get_driver(browser)
    yield driver
    driver.quit()