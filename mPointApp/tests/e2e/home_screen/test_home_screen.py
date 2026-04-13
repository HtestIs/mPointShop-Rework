import allure
import pytest
@pytest.mark.mpointapp
@pytest.mark.e2e
@pytest.mark.defect
@allure.feature("Registration")
@allure.story("Happy path")
@allure.title("Register successfully with valid phone, OTP, and password")
@allure.severity(allure.severity_level.CRITICAL)
def test_navigate_to_voucher_section(login_valid_user):
    home_screen = login_valid_user
    voucher_screen = home_screen.click_see_more_voucher()
    assert voucher_screen.is_voucher_page_displayed(), "Voucher page should be displayed after clicking 'See more vouchers'"
