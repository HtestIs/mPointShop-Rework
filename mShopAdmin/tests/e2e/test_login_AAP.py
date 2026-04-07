from mShopAdmin.pages.login_page import LoginPage
import pytest

@pytest.mark.e2e
@pytest.mark.ongoing
def test_login_valid_aap(driver, env_config):
    login_page = LoginPage(driver)
    login_page.open_url()
    login_page.fill_login(env_config["aap_username"], env_config["aap_password"])
    assert "/#/dashboard" in login_page.get_current_url(), "User is not redirected to dashboard after login"
