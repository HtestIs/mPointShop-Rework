import allure
import pytest

from mPointApp.pages.home_screen import AppHomePage
@pytest.mark.mpointapp
@pytest.mark.e2e
@allure.feature("Registration")
@allure.story("Happy path")
@allure.title("Register successfully with valid phone, OTP, and password")
@allure.severity(allure.severity_level.CRITICAL)
def test_navigate_to_voucher_section(login_valid_user):
    home_screen = login_valid_user
    home_screen.click_see_more_voucher()
    assert home_screen.is_voucher_section_displayed(), "Voucher section should be visible after clicking 'See more'."