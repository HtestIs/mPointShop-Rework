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
    invalid =voucher_scan_page.get_invalid_store_message()
    assert invalid == "Mã voucher không áp dụng cho cửa hàng này", "Expected invalid store message not displayed"

@pytest.mark.e2e
@pytest.mark.api
@allure.feature("Voucher Redemption")
@allure.story("Voucher redemption flow")
@allure.title("Merchant can redeem voucher from all systems")
@allure.severity(allure.severity_level.CRITICAL)
def test_redeem_voucher_valid(login_valid_merchant_success):
                              #,create_voucher_discount_constant,mpointshop_logged_in_client_partner,mexchange_client_ui,mshopadmin_api_client_with_token,app_logged_in_client):
    # response = create_voucher_discount_constant
    # code = get_code(response,mpointshop_logged_in_client_partner,mexchange_client_ui,mshopadmin_api_client_with_token,app_logged_in_client)
    menu = login_valid_merchant_success
    voucher_scan_page = menu.navigate_to_voucher_scan()
    assert voucher_scan_page.is_loaded(), "Voucher scan page did not load successfully"
    voucher_scan_page.enter_voucher("P0O9Y4G9CA")
    voucher_scan_page.click_confirm()
    voucher_scan_page.enter_total_bill(100000)
    max = voucher_scan_page.get_max_bill_amount()
    discount = voucher_scan_page.get_discount_amount()
    final = voucher_scan_page.get_final_bill_amount()
    print(f"Max bill amount: {max}, Discount amount: {discount}, Final bill amount: {final}")
