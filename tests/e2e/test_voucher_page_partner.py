import pytest
import allure

from api.endpoints.voucher_api import VoucherAPI

@pytest.mark.ongoing
@pytest.mark.e2e
@pytest.mark.api
@allure.story("Voucher page")
@allure.title("Partner can create voucher")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("voucher_type",[
    "cash_multiple", 
    "discount_percentage", 
    "discount_constant", 
    "gift"],ids=["Pre-paid voucher","Percentage discount voucher","Constant discount voucher","Gift voucher"])
def test_partner_create_voucher_page(voucher_data, logged_in_client_partner,login_partner_success,voucher_type): ## <--- delete this
    # Step 1: Create voucher page
    voucher_page = VoucherAPI(client = logged_in_client_partner)
    payload = voucher_data(vouchertype=voucher_type)
    response = voucher_page.create_voucher(payload=payload)
    assert response.status_code == 200
    menu = login_partner_success
    voucher_ui = menu.navigate_to_voucher_manage()
    voucher_ui.search_voucher_and_wait(payload["name"])
    first_voucher_name = voucher_ui.get_first_voucher_name()
    print("Voucher name on UI:", first_voucher_name)
    assert payload["name"] == first_voucher_name, "Voucher name on UI does not match created voucher name"