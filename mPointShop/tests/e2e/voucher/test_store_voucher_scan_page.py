import pytest
import allure
from time import sleep

from core.utils.shared_voucher_flows import get_code

pytestmark = [
    pytest.mark.mpointshop,
    allure.parent_suite("mPointShop"),
    allure.suite("E2E"),
    allure.sub_suite("Voucher"),
]

@pytest.mark.e2e
@pytest.mark.api
@pytest.mark.mpointapp
@pytest.mark.mexchange
@allure.feature("Voucher Redemption")
@allure.story("Voucher redemption flow")
@allure.title("Merchant can redeem voucher from all systems")
@allure.severity(allure.severity_level.CRITICAL)
def test_redeem_voucher(login_merchant_success,create_voucher_discount_percentage,mpointshop_logged_in_client_partner,mexchange_client_ui,mshopadmin_api_client_with_token,app_logged_in_client):
    response = create_voucher_discount_percentage
    code = get_code(response,mpointshop_logged_in_client_partner,mexchange_client_ui,mshopadmin_api_client_with_token,app_logged_in_client)
    menu = login_merchant_success
    voucher_scan_page = menu.navigate_to_voucher_scan()
    assert voucher_scan_page.is_loaded(), "Voucher scan page did not load successfully"
    voucher_scan_page.enter_voucher(code)
    voucher_scan_page.click_confirm()
    sleep(2)  # Wait for the redemption process to complete