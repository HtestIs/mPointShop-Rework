import pytest
import allure

from api.endpoints.voucher_api import VoucherAPI

@pytest.mark.ongoing
@allure.story("Voucher page")
@allure.title("Partner can create voucher page")
@allure.severity(allure.severity_level.CRITICAL)

def test_partner_create_voucher_page(voucher_data, logged_in_client_partner, login_partner_success): ## <--- delete this
    # Step 1: Create voucher page
    voucher_page = VoucherAPI(client = logged_in_client_partner)
    payload = voucher_data.copy()
    response = voucher_page.create_voucher(payload=payload)
    assert response.status_code == 200
    uilogin = login_partner_success
    voucher_ui = uilogin.navigate_to_voucher_manage()
    voucher_ui.search_voucher_and_wait(payload["name"])
    first_voucher_name = voucher_ui.get_first_voucher_name()
    print("Voucher name on UI:", first_voucher_name)
    assert payload["name"] == first_voucher_name, "Voucher name on UI does not match created voucher name"