import os

import pytest

from core.drivers.driver_manager import DriverManager


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    is_ci = os.getenv("CI", "").lower() == "true"
    cli_headless = request.config.getoption("--headless")
    driver = DriverManager.get_driver(
        browser,
        headless=cli_headless or is_ci
    )
    if request.node.get_closest_marker("mexchange"):
        base_url = request.getfixturevalue("mexchange_base_url")
    elif request.node.get_closest_marker("mshopadmin"):
        base_url = request.getfixturevalue("mshopadmin_base_url")
    else:
        base_url = request.getfixturevalue("mpointshop_base_url")

    driver.base_url = base_url
    yield driver
    driver.quit()

