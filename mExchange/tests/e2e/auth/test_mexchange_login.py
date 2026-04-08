import allure
import pytest

from mExchange.pages.base_page import BasePage
from mExchange.pages.menu_page import MenuPage

pytestmark = [
    pytest.mark.mexchange,
    allure.parent_suite("mExchange"),
    allure.suite("E2E"),
    allure.sub_suite("Authentication"),
]


@allure.feature("Login authentication")
@pytest.mark.smoke
@pytest.mark.defect
@pytest.mark.e2e
@allure.story("Login with token")
@allure.title("Test mExchange login with injected token")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_with_token_then_ui(self, driver, env_config, mexchange_token_from_ui):
    auth = BasePage(driver)
    auth.open(env_config["mexchange_web_url"])
    auth.dump_token(mexchange_token_from_ui)
    auth.refresh_page()

    menu_page = MenuPage(driver)
    menu_page.wait_url()

    assert "/#/dashboard" in menu_page.get_current_url(), (
        f"Expected mExchange dashboard to load after setting token, but got '{menu_page.get_current_url()}'"
    )
